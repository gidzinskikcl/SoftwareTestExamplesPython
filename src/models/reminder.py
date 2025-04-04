from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Reminder(Base):
    __tablename__ = 'reminders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    reminder_time = Column(DateTime, nullable=False)
    message = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)  # Reminder belongs to an event
    
    event = relationship("Event", back_populates="reminders")

    def __init__(self, reminder_time, message, event_id):
        self.reminder_time = reminder_time
        self.message = message
        self.event_id = event_id

    def __repr__(self):
        return f"<Reminder(message={self.message}, reminder_time={self.reminder_time})>"

    def is_past_due(self):
        """Check if the reminder time has already passed."""
        return self.reminder_time < datetime.now()
