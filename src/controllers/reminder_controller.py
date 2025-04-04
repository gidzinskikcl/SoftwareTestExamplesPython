from src.models.reminder import Reminder
from src.models.event import Event

class ReminderController:
    def __init__(self, reminder_model, event_model):
        self.reminder_model = reminder_model
        self.event_model = event_model

    def create_reminder(self, reminder):
        """Create a new reminder."""
        self.reminder_model.session.add(reminder)
        self.reminder_model.session.commit()

    def get_reminders_for_event(self, event_id):
        """Get all reminders for a specific event."""
        return self.reminder_model.query.filter_by(event_id=event_id).all()

    def delete_reminder(self, reminder_id):
        """Delete a reminder."""
        reminder = self.reminder_model.query.get(reminder_id)
        if reminder:
            self.reminder_model.session.delete(reminder)
            self.reminder_model.session.commit()
