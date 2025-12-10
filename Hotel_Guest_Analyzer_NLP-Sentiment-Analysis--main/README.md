# Hotel Guest Sentiment Analysis - NLP Project

## 📋 Project Overview

This project implements a complete NLP-based sentiment analysis system for hotel guest reviews, including both a Jupyter Notebook for analysis and a Flask web application with user authentication for real-time sentiment analysis.

## 🎯 Problem Statement

A leading hotel chain faces the challenge of managing guest feedback efficiently across multiple booking platforms. With thousands of reviews containing valuable insights, manual analysis is time-consuming. This project provides an NLP-based sentiment analysis approach to quickly and accurately assess guest sentiment from reviews.

## 🎯 Objective

Leverage sentiment analysis to extract actionable insights from guest reviews, enabling the hotel chain to:
- Optimize services and enhance guest experiences
- Identify common pain points and satisfaction trends
- Make data-driven decisions for service improvement
- Increase guest satisfaction and repeat business

## 📚 Prerequisites

### Software Requirements
- **Python 3.7+**
- **Jupyter Notebook** or **Google Colab**
- **Anaconda Navigator** (recommended for local development)
- **Web Browser** (for Flask app)

### Installation Steps

#### Quick Setup (Recommended)

1. **Run the setup script**:
   ```bash
   python setup_environment.py
   ```
   This will automatically:
   - Check Python version
   - Install all required packages
   - Download NLTK data
   - Verify dataset
   - Create necessary directories

#### Manual Setup

1. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

2. **Download NLTK Data** (run once)
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('vader_lexicon')
   ```

3. **Verify Installation**
   ```bash
   python -c "import pandas, numpy, flask, textblob; print('All packages installed!')"
   ```

## 📁 Project Structure

```
Hotel_Guest_Analyser_NLP/
│
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── setup_environment.py              # Environment setup script
├── run.py                             # Flask application runner
├── app.py                             # Alternative entry point
├── config.py                          # Configuration settings
│
├── hotel_sentiment_analysis.ipynb     # Jupyter notebook for analysis
│
├── app/                               # Flask application package
│   ├── __init__.py                    # Flask app initialization
│   ├── routes.py                      # Application routes
│   ├── models.py                      # Database models
│   ├── sentiment_analyzer.py         # Sentiment analysis logic
│   └── auth.py                        # Authentication helpers
│
├── templates/                          # Jinja2 HTML templates
│   ├── base.html                      # Base template
│   ├── index.html                     # Home page
│   ├── login.html                     # Login page
│   ├── signup.html                    # Signup page
│   ├── dashboard.html                 # User dashboard
│   ├── analyze.html                   # Sentiment analysis page
│   └── dataset_analysis.html          # Dataset analysis results
│
├── static/                            # Static files
│   └── css/
│       └── style.css                  # Custom styles
│
├── data/                              # Dataset files
│   └── hotel_reviews_dataset.csv      # Real-world hotel reviews (100 reviews)
│
└── instance/                          # Instance-specific files
    └── database.db                    # SQLite database (created automatically)
```

## 🚀 Project Tasks Breakdown

### Task 1: Data Collection and Preparation

**Objective**: Collect guest reviews and prepare them for analysis by cleaning and preprocessing.

**Steps**:
1. Load reviews from data source (CSV, TXT, or API)
2. Convert text to lowercase
3. Remove special characters and punctuation
4. Remove extra whitespace
5. Store cleaned reviews

**Implementation**:
- Text normalization
- Character filtering (keep only alphanumeric and whitespace)
- Data validation

**Expected Output**: Clean, normalized review text ready for sentiment analysis

---

### Task 2: Sentiment Analysis

**Objective**: Classify reviews as positive, negative, or neutral using NLP techniques.

**Approach**: 
- Use TextBlob library for sentiment polarity analysis
- Polarity range: -1 (very negative) to +1 (very positive)
- Classification thresholds:
  - **Positive**: polarity > 0
  - **Negative**: polarity < 0
  - **Neutral**: polarity = 0

**Implementation**:
- Sentiment polarity calculation
- Sentiment classification
- Result aggregation

**Expected Output**: List of sentiment labels for each review

---

### Task 3: Visualizing Sentiment Distribution

**Objective**: Create visualizations to understand sentiment distribution across reviews.

**Visualizations**:
1. **Bar Chart**: Count of positive, negative, and neutral reviews
2. **Pie Chart**: Percentage distribution of sentiments
3. **Statistics Summary**: Counts and percentages

**Implementation**:
- Sentiment counting
- Data aggregation
- Chart generation using Matplotlib

**Expected Output**: Visual charts showing sentiment distribution

## 🌐 Web Application Features

### Authentication System
- **User Registration**: New users can create accounts
- **User Login**: Secure login with session management
- **User Dashboard**: Personalized dashboard for logged-in users
- **Session Management**: Secure session handling with Flask-Login

### Sentiment Analysis Features
- **Single Review Analysis**: Analyze individual reviews
- **Batch Analysis**: Upload and analyze multiple reviews
- **Real-time Results**: Instant sentiment classification
- **Visualization**: Charts and graphs for sentiment distribution
- **Export Results**: Download analysis results

## 🔧 Usage Instructions

### Option 1: Jupyter Notebook Analysis

1. **Open Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Navigate to project directory** and open `hotel_sentiment_analysis.ipynb`

3. **Run cells sequentially** to:
   - Prepare data
   - Perform sentiment analysis
   - Visualize results

### Option 2: Flask Web Application

1. **Initialize the database** (first time only):
   ```bash
   python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
   ```

2. **Run the Flask application**:
   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

4. **Use the application**:
   - Sign up for a new account
   - Log in with your credentials
   - Navigate to "Analyze Reviews"
   - Enter or upload reviews for sentiment analysis

### Option 3: Google Colab

1. Upload `hotel_sentiment_analysis.ipynb` to Google Colab
2. Install required libraries in first cell:
   ```python
   !pip install numpy pandas nltk textblob matplotlib seaborn
   ```
3. Run all cells

## 📊 Libraries Used

### Core Libraries
- **NumPy**: Numerical operations and array handling
- **Pandas**: Data manipulation and analysis
- **NLTK**: Natural Language Processing toolkit
- **TextBlob**: Sentiment analysis

### Visualization
- **Matplotlib**: Data visualization
- **Seaborn**: Enhanced visualizations

### Web Framework
- **Flask**: Web application framework
- **Flask-Login**: User session management
- **Werkzeug**: Security utilities (password hashing)

## 📈 Expected Results

### Jupyter Notebook Output
- Cleaned and preprocessed reviews
- Sentiment labels for each review
- Bar charts and pie charts showing sentiment distribution
- Summary statistics

### Web Application Output
- User authentication and dashboard
- Real-time sentiment analysis results
- Interactive visualizations
- Downloadable analysis reports

## 🎓 Learning Outcomes

By completing this project, you will learn:

1. **NLP Fundamentals**:
   - Text preprocessing techniques
   - Sentiment analysis concepts
   - Text classification methods

2. **Data Science Skills**:
   - Data cleaning and preparation
   - Statistical analysis
   - Data visualization

3. **Web Development**:
   - Flask framework
   - User authentication
   - RESTful API design
   - Frontend-backend integration

4. **Python Programming**:
   - Working with NLP libraries
   - Data manipulation with Pandas
   - Creating visualizations
   - Building web applications

## 🔍 Future Enhancements

1. **Advanced Sentiment Analysis**:
   - Aspect-based sentiment analysis (room, service, food, etc.)
   - Emotion detection
   - Multi-class classification

2. **Machine Learning Integration**:
   - Train custom sentiment classifier
   - Use pre-trained models (BERT, RoBERTa)
   - Improve accuracy with domain-specific training

3. **Advanced Features**:
   - Review history for users
   - Export to CSV/PDF
   - Email notifications
   - API endpoints for integration

4. **Deployment**:
   - Deploy to cloud (Heroku, AWS, GCP)
   - Docker containerization
   - CI/CD pipeline

## 🐛 Troubleshooting

### Common Issues

1. **NLTK Data Not Found**:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

2. **TextBlob Installation Issues**:
   ```bash
   pip install textblob
   python -m textblob.download_corpora
   ```

3. **Flask App Not Running**:
   - Check if port 5000 is available
   - Ensure all dependencies are installed
   - Check for syntax errors in app.py

## 📝 Notes

- Ensure you have sufficient data (minimum 50-100 reviews for meaningful analysis)
- TextBlob works best with English text
- For production use, consider using a more robust database (PostgreSQL)
- Implement proper error handling and validation
- Add rate limiting for API endpoints

## 🤝 Contributing

Feel free to enhance this project by:
- Adding more sophisticated sentiment analysis methods
- Improving visualizations
- Adding new features
- Optimizing code performance
- Enhancing UI/UX

## 📄 License

This project is for educational purposes.

---

**Happy Analyzing! 🎉**
