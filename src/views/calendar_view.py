from flask import render_template
from datetime import datetime, timedelta
from src.models.event import Event
from src.controllers.calendar_controller import CalendarController

class CalendarView:
    def __init__(self, controller: CalendarController):
        self.controller = controller
    
    def render_day_view(self, user, day=None):
        """Render the day view for the user."""
        day = day or datetime.today()
        events = self.controller.get_events_for_day(user, day)
        return render_template('calendar/day_view.html', events=events, date=day)

    def render_week_view(self, user, week_start=None):
        """Render the week view for the user."""
        week_start = week_start or self.controller.get_start_of_week(datetime.today())
        events = self.controller.get_events_for_week(user, week_start)
        return render_template('calendar/week_view.html', events=events, week_start=week_start)

    def render_month_view(self, user, month=None):
        """Render the month view for the user."""
        month = month or datetime.today().month
        events = self.controller.get_events_for_month(user, month)
        return render_template('calendar/month_view.html', events=events, month=month)

    def render_event_detail(self, user, event_id):
        """Render event detail page."""
        event = self.controller.get_event_by_id(event_id)
        if event and event.user_id == user.id:
            return render_template('calendar/event_detail.html', event=event)
        else:
            return "Event not found or access denied", 404
