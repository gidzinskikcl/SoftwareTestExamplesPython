from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base

# Database configuration (for example, using SQLite in this case)
DATABASE_URL = 'sqlite:///calendar_app.db'  # Change to your preferred DB (e.g., PostgreSQL, MySQL)

# Create an engine and session factory
engine = create_engine(DATABASE_URL, echo=True)
SessionFactory = sessionmaker(bind=engine)

# Function to create a new database session
def db_session():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()
