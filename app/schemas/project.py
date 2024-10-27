from pydantic import BaseModel
from typing import List
from datetime import datetime

class ProjectBase(BaseModel):
    """Base Project schema with common attributes"""
    title: str
    description: str
    tags: List[str]
    user_id: int

class ProjectCreate(ProjectBase):
    """Schema for creating a new project"""
    pass

class ProjectResponse(ProjectBase):
    """Schema for project responses"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
