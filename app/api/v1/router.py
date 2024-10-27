from fastapi import APIRouter
from app.api.v1.endpoints import projects, users

api_router = APIRouter()

# Include routers from endpoints
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
