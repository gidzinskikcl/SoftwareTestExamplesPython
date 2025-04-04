from flask import session, redirect, url_for, flash
from src.models.user import User

class SessionManager:
    def __init__(self, user_model):
        self.user_model = user_model

    def get_logged_in_user(self):
        """Retrieve the logged-in user by their session ID."""
        user_id = session.get('user_id')
        if user_id:
            user = self.user_model.query.get(user_id)
            return user
        return None

    def is_logged_in(self):
        """Check if the user is currently logged in."""
        return self.get_logged_in_user() is not None

    def require_login(self):
        """Redirect to login page if the user is not logged in."""
        if not self.is_logged_in():
            flash("You must be logged in to access this page.", "warning")
            return redirect(url_for('user.render_login'))  # Redirect to login page
        return None  # No redirection, meaning the user is logged in
