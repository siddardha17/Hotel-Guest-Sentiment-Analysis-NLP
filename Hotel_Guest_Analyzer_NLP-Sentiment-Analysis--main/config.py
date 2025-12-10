"""
Configuration file for Flask application
"""
import os
from pathlib import Path

# Get the base directory
basedir = Path(__file__).parent.absolute()
instance_path = basedir / 'instance'
instance_path.mkdir(exist_ok=True)

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    # Use absolute path to avoid issues with spaces in path
    database_path = instance_path / 'database.db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{database_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

