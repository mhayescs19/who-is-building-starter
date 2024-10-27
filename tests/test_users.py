from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.crud import crud_user
from app.schemas.user import UserCreate

def test_create_user(client: TestClient, db: Session):
    data = {
        "email": "test@example.com",
        "password": "testpassword",
        "name": "Test User",
        "gitHubUsername": "testuser",
        "socials": ["https://github.com/testuser"],
        "expertise": ["Python", "FastAPI"]
    }
    response = client.post("/api/v1/users/", json=data)
    assert response.status_code == 201
    content = response.json()
    assert content["email"] == data["email"]
    assert content["name"] == data["name"]
    assert "id" in content

def test_get_users(client: TestClient, db: Session):
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
