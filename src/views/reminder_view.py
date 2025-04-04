from flask import render_template, request, redirect, url_for
from datetime import datetime
from src.models.reminder import Reminder
from src.controllers.reminder_controller import ReminderController

class ReminderView:
    def __init__(self, controller: ReminderController):
        self.controller = controller

    def render_create_reminder(self, event_id):
        """Render the form to create a reminder for an event."""
        return render_template('reminder/create_reminder.html', event_id=event_id)

    def handle_create_reminder(self, event_id):
        """Handle the form submission for creating a new reminder."""
        reminder_time = datetime.strptime(request.form.get('reminder_time'), "%Y-%m-%d %H:%M")
        message = request.form.get('message')

        new_reminder = Reminder(reminder_time, message, event_id)
        self.controller.create_reminder(new_reminder)
        return redirect(url_for('calendar.render_event_detail', event_id=event_id))

    def render_reminders_for_event(self, event_id):
        """Render reminders for a specific event."""
        reminders = self.controller.get_reminders_for_event(event_id)
        return render_template('reminder/reminders_for_event.html', reminders=reminders)
