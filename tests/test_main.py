from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_content():
    response = client.get("/")
    data = response.json()
    assert "mensagem" in data
    assert data["status"] == "online"
    assert data["versao"] == "1.0.0"


def test_health_status_code():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_content():
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "healthy"
