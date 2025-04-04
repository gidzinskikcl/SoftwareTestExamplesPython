# This file will initialize the authentication module when imported.
from .login import LoginHandler
from .registration import RegistrationHandler
from .session import SessionManager
from .oauth import OAuthHandler  # Optional, for OAuth integration (e.g., Google, Facebook)
