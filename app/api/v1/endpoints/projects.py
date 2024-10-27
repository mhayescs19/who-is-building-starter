from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.project import ProjectCreate, ProjectResponse
from app.crud import crud_project

router = APIRouter()

@router.get("/", response_model=List[ProjectResponse])
def get_all_projects(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve all projects.
    """
    return crud_project.get_multi(db, skip=skip, limit=limit)

# ... (rest of the project routes)
