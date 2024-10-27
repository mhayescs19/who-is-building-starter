from sqlalchemy import Column, Integer, String, DateTime, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    tags = Column(ARRAY(String))
    user_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    owner = relationship("User", back_populates="projects")
