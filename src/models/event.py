from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String, nullable=True)
    recurrence = Column(Enum("daily", "weekly", "monthly", name="recurrence_types"), nullable=True)
    category = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Relationship with User

    user = relationship("User", back_populates="events")

    def __init__(self, name, start_time, end_time, category, recurrence=None, description=None, location=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.category = category
        self.recurrence = recurrence
        self.description = description
        self.location = location

    def __repr__(self):
        return f"<Event(name={self.name}, start_time={self.start_time}, category={self.category})>"

    def duration(self):
        """Returns the duration of the event."""
        return (self.end_time - self.start_time).seconds / 60  # Duration in minutes

    def is_recurring(self):
        """Check if the event is recurring."""
        return self.recurrence is not None
