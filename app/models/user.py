from sqlalchemy import Column, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    github_username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    socials = Column(ARRAY(String))
    expertise = Column(ARRAY(String))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    projects = relationship("Project", back_populates="owner")
