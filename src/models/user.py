from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    is_member = Column(Boolean, default=False)  # Membership status (e.g., Regular, Member)
    
    events = relationship("Event", back_populates="user", cascade="all, delete-orphan")

    def __init__(self, email, password, name=None, is_member=False):
        self.email = email
        self.password = password
        self.name = name
        self.is_member = is_member

    def __repr__(self):
        return f"<User(email={self.email}, name={self.name})>"

    def check_password(self, password):
        """Check if the provided password matches the stored password."""
        return self.password == password  # This is for simplicity, you should hash the password in production.

    def get_membership_discount(self):
        """Return a discount based on membership."""
        if self.is_member:
            return 0.15  # 15% discount for members
        return 0  # No discount for non-members
    