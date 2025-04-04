from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from src.auth import LoginHandler, RegistrationHandler, SessionManager
from src.controllers.event_controller import EventController
from src.controllers.user_controller import UserController
from src.views import CalendarView, EventView, UserView
from src.models import User, Event, Reminder
from src.database.db import db_session, engine
from flask import flash

app = Flask(__name__)

# Configurations for the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar_app.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this for production
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize extensions
db = SQLAlchemy(app)
Session(app)

# Initialize handlers, controllers, and views
login_handler = LoginHandler(User)
registration_handler = RegistrationHandler(User)
session_manager = SessionManager(User)
event_controller = EventController(Event, User)
user_controller = UserController(User)

calendar_view = CalendarView(event_controller)
event_view = EventView(event_controller)
user_view = UserView(registration_handler, login_handler)

# Create tables in the database
@app.before_first_request
def init_db():
    # Create all tables
    User.metadata.create_all(engine)
    Event.metadata.create_all(engine)
    Reminder.metadata.create_all(engine)

# Home route: Redirect to the login page
@app.route('/')
def home():
    if session_manager.is_logged_in():
        return redirect(url_for('calendar.render_month_view'))
    return redirect(url_for('user.render_login'))

# Login routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return login_handler.login_user(email, password)
    return render_template('user/login.html')

# Logout route
@app.route('/logout')
def logout():
    return login_handler.logout_user()

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form.get('name')
        return registration_handler.register_user(email, password, name)
    return render_template('user/register.html')

# Calendar routes
@app.route('/calendar/month', methods=['GET', 'POST'])
def render_month_view():
    user = session_manager.get_logged_in_user()
    return calendar_view.render_month_view(user)

@app.route('/calendar/week', methods=['GET', 'POST'])
def render_week_view():
    user = session_manager.get_logged_in_user()
    return calendar_view.render_week_view(user)

@app.route('/calendar/day', methods=['GET', 'POST'])
def render_day_view():
    user = session_manager.get_logged_in_user()
    return calendar_view.render_day_view(user)

# Event routes
@app.route('/event/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        category = request.form['category']
        recurrence = request.form['recurrence']
        location = request.form.get('location')

        new_event = Event(name=name, description=description, start_time=start_time, end_time=end_time,
                          category=category, recurrence=recurrence, location=location)
        event_controller.create_event(new_event)
        flash("Event created successfully!", "success")
        return redirect(url_for('calendar.render_month_view'))
    return render_template('event/create_event.html')

@app.route('/event/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = event_controller.get_event_by_id(event_id)
    if request.method == 'POST':
        event.name = request.form['name']
        event.description = request.form['description']
        event.start_time = request.form['start_time']
        event.end_time = request.form['end_time']
        event.category = request.form['category']
        event.recurrence = request.form['recurrence']
        event.location = request.form.get('location')

        event_controller.update_event(event_id, event)
        flash("Event updated successfully!", "success")
        return redirect(url_for('calendar.render_month_view'))
    
    return render_template('event/edit_event.html', event=event)

@app.route('/event/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    event_controller.delete_event(event_id)
    flash("Event deleted successfully!", "success")
    return redirect(url_for('calendar.render_month_view'))

# Error handling routes (optional)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
