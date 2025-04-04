from datetime import datetime, timedelta

def get_next_occurrence_of_event(start_time, recurrence_type):
    """
    Given an event's start time and recurrence type (daily, weekly, monthly),
    returns the next occurrence of that event.
    """
    if recurrence_type == "daily":
        return start_time + timedelta(days=1)
    elif recurrence_type == "weekly":
        return start_time + timedelta(weeks=1)
    elif recurrence_type == "monthly":
        # Move to the same day next month (handle month overflow)
        next_month = start_time.replace(month=start_time.month % 12 + 1)
        return next_month.replace(day=start_time.day)
    else:
        raise ValueError(f"Invalid recurrence type: {recurrence_type}")

def is_event_in_future(event_time):
    """Returns True if the event's time is in the future, otherwise False."""
    return event_time > datetime.now()

def get_day_of_week(date):
    """Returns the day of the week as a string (e.g., 'Monday')."""
    return date.strftime('%A')

def get_week_number(date):
    """Returns the ISO week number for the given date."""
    return date.isocalendar()[1]
