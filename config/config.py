import os

class Config:
    """Base config class with common settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')  # Change this for production
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    DEBUG = os.environ.get('DEBUG', True)

class DevelopmentConfig(Config):
    """Development environment config settings."""
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to reduce overhead
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL', 'sqlite:///dev_calendar.db')

class ProductionConfig(Config):
    """Production environment config settings."""
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///calendar.db')

class TestingConfig(Config):
    """Testing environment config settings."""
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'sqlite:///test_calendar.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
