import os

class DatabaseConfig:
    """Class to hold database configuration settings."""
    @staticmethod
    def get_database_uri(environment='development'):
        """Return the appropriate database URI based on the environment."""
        if environment == 'development':
            return os.environ.get('DEV_DATABASE_URL', 'sqlite:///dev_calendar.db')
        elif environment == 'production':
            return os.environ.get('DATABASE_URL', 'sqlite:///calendar.db')
        elif environment == 'testing':
            return os.environ.get('TEST_DATABASE_URL', 'sqlite:///test_calendar.db')
        else:
            raise ValueError("Invalid environment specified for the database URI.")

