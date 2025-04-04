from src.models.user import User
from flask import session
import hashlib

class UserController:
    def __init__(self, user_model):
        self.user_model = user_model

    def create_user(self, email, password, name=None):
        """Create a new user with hashed password."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(email=email, password=hashed_password, name=name)
        self.user_model.session.add(new_user)
        self.user_model.session.commit()

    def authenticate_user(self, email, password):
        """Authenticate user by email and password."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = self.user_model.query.filter_by(email=email, password=hashed_password).first()
        return user

    def check_if_user_exists(self, email):
        """Check if a user with the given email already exists."""
        return self.user_model.query.filter_by(email=email).first() is not None

    def get_user_by_id(self, user_id):
        """Get user by ID."""
        return self.user_model.query.get(user_id)

    def get_logged_in_user(self):
        """Get the current logged-in user from the session."""
        user_id = session.get('user_id')
        if user_id:
            return self.get_user_by_id(user_id)
        return None
