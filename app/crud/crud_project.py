from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    def get_user_projects(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> list[Project]:
        return db.query(Project).filter(Project.user_id == user_id)\
            .offset(skip).limit(limit).all()
    
    def search(self, db: Session, *, query: str, skip: int = 0, limit: int = 100) -> list[Project]:
        return db.query(Project).filter(
            Project.title.ilike(f"%{query}%") |
            Project.description.ilike(f"%{query}%")
        ).offset(skip).limit(limit).all()

crud_project = CRUDProject(Project)
