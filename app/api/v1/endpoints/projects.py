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

@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Create a new project.
    """
    return crud_project.create(db, obj_in=project)

@router.get("/{id}", response_model=ProjectResponse)
def get_project(
    id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Get a specific project by id.
    """
    project = crud_project.get(db, id=id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "Project not found",
                "code": 404,
                "message": "The project with the provided id does not exist."
            }
        )
    return project

@router.put("/{id}", response_model=ProjectResponse)
def update_project(
    id: int,
    project: ProjectCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Update a project.
    """
    db_project = crud_project.get(db, id=id)
    if not db_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "Project not found",
                "code": 404,
                "message": "The project with the provided id does not exist."
            }
        )
    return crud_project.update(db, db_obj=db_project, obj_in=project)

@router.delete("/{id}", response_model=ProjectResponse)
def delete_project(
    id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Delete a project.
    """
    project = crud_project.get(db, id=id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "Project not found",
                "code": 404,
                "message": "The project with the provided id does not exist."
            }
        )
    return crud_project.remove(db, id=id)

@router.get("/search/{query}", response_model=List[ProjectResponse])
def search_projects(
    query: str,
    db: Session = Depends(deps.get_db)
):
    """
    Search for projects based on a query string.
    """
    return crud_project.search(db, query=query)

# ... (rest of the project routes)
