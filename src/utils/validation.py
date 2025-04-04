import re
from datetime import datetime

def validate_email(email):
    """Validates an email address using a simple regular expression."""
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(email_regex, email):
        return True
    return False

def validate_password(password):
    """Validates a password (at least 8 characters, 1 digit, 1 letter)."""
    if len(password) >= 8 and re.search(r"\d", password) and re.search(r"[A-Za-z]", password):
        return True
    return False

def validate_date(date_str, date_format="%Y-%m-%d"):
    """Validates if a given string can be parsed into a date."""
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False
