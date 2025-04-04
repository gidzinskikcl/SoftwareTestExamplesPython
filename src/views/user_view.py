from flask import render_template, request, redirect, url_for, flash
from src.controllers.user_controller import UserController

class UserView:
    def __init__(self, controller: UserController):
        self.controller = controller
    
    def render_login(self):
        """Render the login page."""
        return render_template('user/login.html')

    def render_register(self):
        """Render the registration page."""
        return render_template('user/register.html')

    def handle_login(self):
        """Handle the login form submission."""
        email = request.form.get('email')
        password = request.form.get('password')

        user = self.controller.authenticate_user(email, password)
        if user:
            return redirect(url_for('calendar.render_month_view'))
        else:
            flash('Invalid login credentials', 'danger')
            return redirect(url_for('user.render_login'))

    def handle_register(self):
        """Handle the registration form submission."""
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        if self.controller.check_if_user_exists(email):
            flash('Email already exists', 'danger')
            return redirect(url_for('user.render_register'))
        
        self.controller.create_user(email, password, name)
        flash('Account created successfully', 'success')
        return redirect(url_for('user.render_login'))
