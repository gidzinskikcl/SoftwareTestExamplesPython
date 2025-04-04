from src.models.event import Event
from src.models.user import User

class EventController:
    def __init__(self, event_model, user_model):
        self.event_model = event_model
        self.user_model = user_model

    def create_event(self, event):
        """Create a new event."""
        self.event_model.session.add(event)
        self.event_model.session.commit()

    def update_event(self, event_id, updated_event):
        """Update an existing event."""
        event = self.event_model.query.get(event_id)
        if event:
            event.name = updated_event.name
            event.start_time = updated_event.start_time
            event.end_time = updated_event.end_time
            event.category = updated_event.category
            event.recurrence = updated_event.recurrence
            event.description = updated_event.description
            event.location = updated_event.location
            self.event_model.session.commit()

    def delete_event(self, event_id):
        """Delete an event."""
        event = self.event_model.query.get(event_id)
        if event:
            self.event_model.session.delete(event)
            self.event_model.session.commit()

    def get_event_by_id(self, event_id):
        """Get a specific event by its ID."""
        return self.event_model.query.get(event_id)
