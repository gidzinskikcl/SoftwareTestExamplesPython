from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Base class for models

# User Model (Table)
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    is_member = Column(Boolean, default=False)

    events = relationship("Event", back_populates="user", cascade="all, delete-orphan")

# Event Model (Table)
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
    reminders = relationship("Reminder", back_populates="event", cascade="all, delete-orphan")

# Reminder Model (Table)
class Reminder(Base):
    __tablename__ = 'reminders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    reminder_time = Column(DateTime, nullable=False)
    message = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)

    event = relationship("Event", back_populates="reminders")

