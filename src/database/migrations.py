from alembic import command
from alembic.config import Config

# Setup the Alembic configuration (path to the Alembic configuration file)
config = Config("alembic.ini")

def run_migrations():
    """Run database migrations using Alembic."""
    command.upgrade(config, 'head')

def create_migration(message="Auto migration"):
    """Generate a new migration script."""
    command.revision(config, message=message, autogenerate=True)

def downgrade_migration():
    """Downgrade the database to the previous version."""
    command.downgrade(config, '-1')
