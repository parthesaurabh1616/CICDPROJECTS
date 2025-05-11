from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Calculator API"}

def test_add():
    response = client.get("/add?a=10&b=5")
    assert response.json() == {"result": 15}

def test_subtract():
    response = client.get("/subtract?a=10&b=5")
    assert response.json() == {"result": 5} 