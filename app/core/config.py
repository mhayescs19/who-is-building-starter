from pydantic_settings import BaseSettings
from typing import List
import secrets

class Settings(BaseSettings):
    """Application settings"""
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "whoIsBuilding.io"
    
    # BACKEND_CORS_ORIGINS is a comma-separated list of origins
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]  # Frontend URL
    
    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/whoisbuilding"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
