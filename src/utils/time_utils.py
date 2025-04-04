from datetime import datetime, timedelta

def get_current_time():
    """Returns the current datetime."""
    return datetime.now()

def get_start_of_week(date):
    """Returns the start of the week (Monday)."""
    return date - timedelta(days=date.weekday())

def get_end_of_week(date):
    """Returns the end of the week (Sunday)."""
    return date + timedelta(days=(6 - date.weekday()))

def get_start_of_month(date):
    """Returns the start of the month."""
    return date.replace(day=1)

def get_end_of_month(date):
    """Returns the end of the month."""
    next_month = date.replace(day=28) + timedelta(days=4)  # Go to the next month, then subtract days
    return next_month - timedelta(days=next_month.day)

def format_date(date, date_format="%Y-%m-%d %H:%M"):
    """Formats a datetime object into a string."""
    return date.strftime(date_format)

def parse_date(date_str, date_format="%Y-%m-%d"):
    """Parses a date string into a datetime object."""
    return datetime.strptime(date_str, date_format)
