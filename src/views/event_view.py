from flask import render_template, request, redirect, url_for
from datetime import datetime
from src.models.event import Event
from src.controllers.event_controller import EventController

class EventView:
    def __init__(self, controller: EventController):
        self.controller = controller

    def render_create_event(self):
        """Render the form to create a new event."""
        return render_template('event/create_event.html')

    def render_edit_event(self, event_id):
        """Render the form to edit an existing event."""
        event = self.controller.get_event_by_id(event_id)
        if event:
            return render_template('event/edit_event.html', event=event)
        else:
            return "Event not found", 404

    def handle_create_event(self):
        """Handle the form submission for creating a new event."""
        name = request.form.get('name')
        start_time = datetime.strptime(request.form.get('start_time'), "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(request.form.get('end_time'), "%Y-%m-%d %H:%M")
        category = request.form.get('category')
        recurrence = request.form.get('recurrence')
        description = request.form.get('description')
        location = request.form.get('location')

        new_event = Event(name, start_time, end_time, category, recurrence, description, location)
        self.controller.create_event(new_event)
        return redirect(url_for('calendar.render_month_view'))

    def handle_edit_event(self, event_id):
        """Handle the form submission for editing an existing event."""
        name = request.form.get('name')
        start_time = datetime.strptime(request.form.get('start_time'), "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(request.form.get('end_time'), "%Y-%m-%d %H:%M")
        category = request.form.get('category')
        recurrence = request.form.get('recurrence')
        description = request.form.get('description')
        location = request.form.get('location')

        updated_event = Event(name, start_time, end_time, category, recurrence, description, location)
        self.controller.update_event(event_id, updated_event)
        return redirect(url_for('calendar.render_month_view'))
