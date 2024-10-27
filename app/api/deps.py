from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/login/access-token")

def get_db() -> Generator:
    """
    Dependency function that yields db sessions
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
