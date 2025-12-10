Hotel Guest Sentiment Analysis – NLP-Based Review Insights
📌 Project Overview

This project delivers a complete NLP-driven system for analyzing sentiments in hotel guest reviews. It includes both:

an exploratory Jupyter Notebook for data analysis, and

an interactive Flask web application featuring user login and real-time review evaluation.

🎯 Problem Statement

Large hotel chains receive thousands of reviews daily from various booking platforms. These reviews contain essential customer insights, but manually analyzing them is slow and inefficient.
This project provides a fully automated NLP solution to quickly interpret guest feedback and determine overall sentiment trends.

🎯 Objectives

Use NLP-based sentiment analysis to extract meaningful insights from hotel reviews, allowing hotel management to:

Improve customer experience through data-driven decisions

Identify recurring issues and service weaknesses

Recognize positive trends and guest satisfaction areas

Enhance overall guest retention and loyalty

📚 Prerequisites
Software Requirements

Python 3.7+

Jupyter Notebook or Google Colab

Anaconda (recommended)

A modern web browser (for the Flask app)
Setup Instructions
🔹 Fast Setup (Recommended)

Run the automatic setup script:python setup_environment.py
This script will:

Verify Python installation

Install all required packages

Download essential NLTK data

Validate the dataset

Create necessary folders
Manual Setup
Install Required Dependencies:pip install -r requirements.txt
Download NLTK Corpora
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
Installation Check
python -c "import pandas, numpy, flask, textblob; print('Environment Ready!')"
Project Directory Structure
Hotel_Guest_Analyser_NLP/
│
├── README.md
├── requirements.txt
├── setup_environment.py
├── run.py
├── app.py
├── config.py
│
├── hotel_sentiment_analysis.ipynb
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── sentiment_analyzer.py
│   └── auth.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── analyze.html
│   └── dataset_analysis.html
│
├── static/
│   └── css/
│       └── style.css
│
├── data/
│   └── hotel_reviews_dataset.csv
│
└── instance/
    └── database.db
Project Workflow
Task 1: Data Cleaning & Preparation

Goal: Prepare raw guest reviews for analysis.

Steps include:

Loading the dataset

Normalizing text (lowercasing)

Removing punctuation and unwanted symbols

Eliminating extra whitespace

Outcome: Clean, structured text ready for sentiment extraction.

Task 2: Sentiment Analysis

Goal: Categorize each review into Positive, Negative, or Neutral.

Method Used

Using TextBlob polarity scores:

0 → Positive

< 0 → Negative

= 0 → Neutral

Processes performed:

Polarity evaluation

Sentiment tagging

Aggregating results

Outcome: Sentiment labels assigned to each review.

Task 3: Sentiment Visualization

Goal: Provide visual insights into sentiment distribution.

Generated Charts

Bar chart showing counts of sentiment classes

Pie chart showing sentiment proportions

Statistical summary table

Outcome: Clear visual breakdown of customer emotions.

🌐 Web Application Features
🔐 User Authentication

Secure signup and login

Protected user sessions

Personalized user dashboard

📊 Sentiment Analysis Tools

Analyze a single review instantly

Upload multiple reviews for batch processing

Graphical sentiment visualization

Option to download analysis results

🔧 How to Use
Option 1: Run Jupyter Notebook
jupyter notebook


Open the notebook and execute cells to:

Clean the dataset

Perform sentiment analysis

Generate charts

Option 2: Run the Flask Web App
Initialize the database (first time only):
python -c "from app import create_app, db; app=create_app(); app.app_context().push(); db.create_all()"

Start the server:
python app.py


Open in browser:

http://localhost:5000


You can then sign up, log in, and begin analyzing reviews.

Option 3: Run on Google Colab

Upload the notebook to Colab

Install dependencies:

!pip install numpy pandas nltk textblob matplotlib seaborn

📊 Key Libraries
Core

NumPy

Pandas

NLTK

TextBlob

Visualization

Matplotlib

Seaborn

Web Framework

Flask

Flask-Login

Werkzeug

📈 Expected Outputs
Notebook Results

Clean dataset

Sentiment categories

Visual sentiment distribution

Summary statistics

Web App Results

Working authentication system

Real-time review classification

Interactive dashboards

Downloadable reports

🎓 Skills Gained
NLP Skills

Text preprocessing

Sentiment classification

Polarity scoring

Data Science Skills

Visualization

Data cleaning

Analysis and interpretation

Web Development Skills

Flask routing

User authentication

Backend–frontend integration

🔮 Future Improvements
NLP Enhancements

Aspect-based sentiment analysis

Emotion detection

Multi-class classification

ML Upgrades

Custom classifier training

Use of transformer models (BERT, RoBERTa)

Feature Extensions

User review history

Export reports (CSV/PDF)

Notification system

Deployment

Cloud deployment (Heroku, AWS, GCP)

Docker support

CI/CD pipeline

🐛 Troubleshooting
Missing NLTK Data
nltk.download('punkt')
nltk.download('stopwords')

TextBlob Issues
pip install textblob
python -m textblob.download_corpora

Flask Not Starting

Ensure port 5000 is free

Check dependency installation

Verify syntax in app.py

🤝 Contributions

You’re welcome to contribute by:

Adding advanced NLP techniques

Improving UI/UX

Optimizing backend logic

Enhancing visualizations
