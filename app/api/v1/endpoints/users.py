from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.user import UserCreate, UserResponse
from app.crud import crud_user

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_all_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve all users.
    """
    return crud_user.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate
):
    """
    Create new user.
    """
    user = crud_user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud_user.create(db, obj_in=user_in)
    return user

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Get a specific user by id.
    """
    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

@router.get("/search/{query}", response_model=List[UserResponse])
def search_users(
    query: str,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Search users.
    """
    users = crud_user.search(db, query=query, skip=skip, limit=limit)
    return users

# ... (rest of the user routes)
