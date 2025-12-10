"""
Application routes
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Analysis
from app.auth import create_user, get_user_by_username
from app.sentiment_analyzer import analyze_sentiment, analyze_batch, get_sentiment_distribution
from werkzeug.security import check_password_hash
import json
import pandas as pd
import os
from collections import Counter

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validation
        if not username or not email or not password:
            flash('All fields are required', 'error')
            return render_template('signup.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('signup.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long', 'error')
            return render_template('signup.html')
        
        # Create user
        user, error = create_user(username, email, password)
        if error:
            flash(error, 'error')
            return render_template('signup.html')
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('routes.login'))
    
    return render_template('signup.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = bool(request.form.get('remember'))
        
        if not username or not password:
            flash('Please enter both username and password', 'error')
            return render_template('login.html')
        
        user = get_user_by_username(username)
        if user and user.check_password(password):
            login_user(user, remember=remember)
            flash(f'Welcome back, {username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('routes.dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('routes.index'))

@bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    # Get user's recent analyses
    recent_analyses = Analysis.query.filter_by(user_id=current_user.id)\
        .order_by(Analysis.created_at.desc())\
        .limit(10)\
        .all()
    
    # Get statistics
    total_analyses = Analysis.query.filter_by(user_id=current_user.id).count()
    positive_count = Analysis.query.filter_by(user_id=current_user.id, sentiment='positive').count()
    negative_count = Analysis.query.filter_by(user_id=current_user.id, sentiment='negative').count()
    neutral_count = Analysis.query.filter_by(user_id=current_user.id, sentiment='neutral').count()
    
    stats = {
        'total': total_analyses,
        'positive': positive_count,
        'negative': negative_count,
        'neutral': neutral_count
    }
    
    return render_template('dashboard.html', 
                         recent_analyses=recent_analyses,
                         stats=stats)

@bp.route('/analyze', methods=['GET', 'POST'])
@login_required
def analyze():
    """Sentiment analysis page"""
    if request.method == 'POST':
        review_text = request.form.get('review_text', '').strip()
        batch_reviews = request.form.get('batch_reviews', '').strip()
        
        if batch_reviews:
            # Batch analysis
            reviews = [r.strip() for r in batch_reviews.split('\n') if r.strip()]
            results = analyze_batch(reviews)
            
            # Save to database
            for result in results:
                analysis = Analysis(
                    user_id=current_user.id,
                    review_text=result['review'],
                    sentiment=result['sentiment'],
                    polarity=result['polarity']
                )
                db.session.add(analysis)
            db.session.commit()
            
            # Calculate distribution
            distribution = get_sentiment_distribution(results)
            
            return render_template('analyze.html', 
                                 results=results,
                                 distribution=distribution,
                                 is_batch=True)
        
        elif review_text:
            # Single review analysis
            result = analyze_sentiment(review_text)
            result['review'] = review_text
            
            # Save to database
            analysis = Analysis(
                user_id=current_user.id,
                review_text=review_text,
                sentiment=result['sentiment'],
                polarity=result['polarity']
            )
            db.session.add(analysis)
            db.session.commit()
            
            # Create complete distribution dictionary
            distribution = {
                'positive': 0,
                'negative': 0,
                'neutral': 0
            }
            distribution[result['sentiment']] = 1
            
            return render_template('analyze.html', 
                                 results=[result],
                                 distribution=distribution,
                                 is_batch=False)
        else:
            flash('Please enter a review to analyze', 'error')
    
    return render_template('analyze.html')

@bp.route('/analyze-dataset', methods=['GET', 'POST'])
@login_required
def analyze_dataset():
    """Analyze the real-world hotel reviews dataset"""
    dataset_path = os.path.join('data', 'hotel_reviews_dataset.csv')
    
    if not os.path.exists(dataset_path):
        flash('Dataset file not found', 'error')
        return redirect(url_for('routes.dashboard'))
    
    try:
        # Load dataset
        df = pd.read_csv(dataset_path)
        
        # Perform sentiment analysis on all reviews
        reviews = df['Cleaned Text (Lowercased)'].dropna().tolist()
        results = analyze_batch(reviews)
        
        # Add review IDs and actual sentiments
        for i, result in enumerate(results):
            if i < len(df):
                result['review_id'] = int(df.iloc[i]['Review ID'])
                result['actual_sentiment'] = df.iloc[i]['Sentiment']
                result['primary_aspect'] = df.iloc[i]['Primary Aspect']
        
        # Calculate statistics
        distribution = get_sentiment_distribution(results)
        
        # Calculate accuracy
        correct = 0
        total = 0
        for result in results:
            if 'actual_sentiment' in result:
                actual = result['actual_sentiment'].lower()
                predicted = result['sentiment']
                # Map mixed to neutral for comparison
                if actual == 'mixed':
                    actual = 'neutral'
                if actual == predicted:
                    correct += 1
                total += 1
        
        accuracy = (correct / total * 100) if total > 0 else 0
        
        # Aspect analysis
        all_aspects = []
        for aspect_str in df['Primary Aspect'].dropna():
            aspects = [a.strip() for a in str(aspect_str).split('&')]
            all_aspects.extend(aspects)
        aspect_counts = Counter(all_aspects)
        top_aspects = dict(aspect_counts.most_common(10))
        
        # Polarity statistics
        polarities = [r['polarity'] for r in results]
        avg_polarity = sum(polarities) / len(polarities) if polarities else 0
        
        # Save sample to database
        for result in results[:10]:  # Save first 10 to database
            analysis = Analysis(
                user_id=current_user.id,
                review_text=result['review'][:500],  # Truncate if too long
                sentiment=result['sentiment'],
                polarity=result['polarity']
            )
            db.session.add(analysis)
        db.session.commit()
        
        return render_template('dataset_analysis.html',
                             results=results,
                             distribution=distribution,
                             accuracy=round(accuracy, 2),
                             total_reviews=len(results),
                             top_aspects=top_aspects,
                             avg_polarity=round(avg_polarity, 3))
    
    except Exception as e:
        flash(f'Error analyzing dataset: {str(e)}', 'error')
        return redirect(url_for('routes.dashboard'))

@bp.route('/api/analyze', methods=['POST'])
@login_required
def api_analyze():
    """API endpoint for sentiment analysis"""
    data = request.get_json()
    review_text = data.get('text', '').strip()
    
    if not review_text:
        return jsonify({'error': 'No text provided'}), 400
    
    result = analyze_sentiment(review_text)
    
    # Save to database
    analysis = Analysis(
        user_id=current_user.id,
        review_text=review_text,
        sentiment=result['sentiment'],
        polarity=result['polarity']
    )
    db.session.add(analysis)
    db.session.commit()
    
    return jsonify(result)

