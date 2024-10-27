from typing import Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def get_by_github_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.github_username == username).first()
    
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            name=obj_in.name,
            github_username=obj_in.gitHubUsername,
            socials=obj_in.socials,
            expertise=obj_in.expertise
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def search(self, db: Session, *, query: str, skip: int = 0, limit: int = 100) -> list[User]:
        return db.query(User).filter(
            User.name.ilike(f"%{query}%") |
            User.github_username.ilike(f"%{query}%") |
            User.email.ilike(f"%{query}%")
        ).offset(skip).limit(limit).all()

crud_user = CRUDUser(User)
