from datetime import datetime, timedelta
from src.models.event import Event
from src.models.user import User

class CalendarController:
    def __init__(self, event_model, user_model):
        self.event_model = event_model
        self.user_model = user_model

    def get_events_for_day(self, user, day):
        """Get all events for a specific day."""
        start_of_day = datetime.combine(day, datetime.min.time())
        end_of_day = start_of_day + timedelta(days=1)
        return self.event_model.query.filter(
            Event.user_id == user.id,
            Event.start_time >= start_of_day,
            Event.start_time < end_of_day
        ).all()

    def get_start_of_week(self, date):
        """Get the start date of the week (Monday)."""
        start_of_week = date - timedelta(days=date.weekday())  # Monday of the current week
        return start_of_week

    def get_events_for_week(self, user, week_start):
        """Get all events for a specific week."""
        week_end = week_start + timedelta(days=7)
        return self.event_model.query.filter(
            Event.user_id == user.id,
            Event.start_time >= week_start,
            Event.start_time < week_end
        ).all()

    def get_events_for_month(self, user, month):
        """Get all events for a specific month."""
        current_year = datetime.today().year
        start_of_month = datetime(current_year, month, 1)
        end_of_month = (start_of_month + timedelta(days=32)).replace(day=1)
        return self.event_model.query.filter(
            Event.user_id == user.id,
            Event.start_time >= start_of_month,
            Event.start_time < end_of_month
        ).all()

    def get_event_by_id(self, event_id):
        """Get a specific event by its ID."""
        return self.event_model.query.get(event_id)

    def get_events_for_user(self, user):
        """Get all events for a specific user."""
        return self.event_model.query.filter_by(user_id=user.id).all()
