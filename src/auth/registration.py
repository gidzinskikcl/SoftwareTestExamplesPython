from flask import flash, redirect, url_for
from src.models.user import User
import hashlib

class RegistrationHandler:
    def __init__(self, user_model):
        self.user_model = user_model

    def is_email_taken(self, email):
        """Check if the email is already registered."""
        return self.user_model.query.filter_by(email=email).first() is not None

    def register_user(self, email, password, name=None):
        """Register a new user after validating the input."""
        if self.is_email_taken(email):
            flash("Email is already taken. Please choose a different one.", "danger")
            return redirect(url_for('user.render_register'))  # Redirect back to registration form
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password before storing
        new_user = User(email=email, password=hashed_password, name=name)
        self.user_model.session.add(new_user)
        self.user_model.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('user.render_login'))  # Redirect to login page after successful registration
