from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class UserBase(BaseModel):
    """Base User schema with common attributes"""
    name: str
    gitHubUsername: str
    email: EmailStr
    socials: List[str]
    expertise: List[str]

class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str

class UserResponse(UserBase):
    """Schema for user responses"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
