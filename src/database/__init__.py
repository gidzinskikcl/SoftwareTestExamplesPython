# This file will initialize the database connection when imported
from .db import db_session, engine
from .schema import Base

def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)  # Create all tables in the database

    # Additional setup logic can be added here (e.g., adding initial admin user)
