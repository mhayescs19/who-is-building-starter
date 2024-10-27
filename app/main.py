from fastapi import FastAPI
from app.routes import project_routes, user_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="whoIsBuilding.io",
    description="An interactive web platform for CS students to showcase and collaborate on projects",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(project_routes.router)
app.include_router(user_routes.router)

@app.get("/")
async def root():
    """Root endpoint returning API information"""
    return {
        "message": "Welcome to whoIsBuilding.io API",
        "version": "1.0.0",
        "documentation": "/docs"
    }
