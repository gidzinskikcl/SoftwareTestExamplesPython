from flask import session, redirect, url_for, flash
from src.models.user import User
import hashlib

class LoginHandler:
    def __init__(self, user_model):
        self.user_model = user_model

    def authenticate(self, email, password):
        """Authenticate the user by email and password."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = self.user_model.query.filter_by(email=email, password=hashed_password).first()
        return user

    def login_user(self, email, password):
        """Login the user by validating credentials and starting a session."""
        user = self.authenticate(email, password)
        if user:
            session['user_id'] = user.id  # Store user ID in the session
            flash("Login successful!", "success")
            return redirect(url_for('calendar.render_month_view'))  # Redirect to calendar view (example)
        else:
            flash("Invalid credentials, please try again.", "danger")
            return redirect(url_for('user.render_login'))  # Redirect back to login page

    def logout_user(self):
        """Logout the user by clearing the session."""
        session.pop('user_id', None)
        flash("You have been logged out.", "info")
        return redirect(url_for('user.render_login'))  # Redirect to login page after logout
