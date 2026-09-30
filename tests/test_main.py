from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_greeting_uses_the_name_parameter():
    response = client.get("/api/greeting", params={"name": "Raj"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Raj!"}


def test_greeting_defaults_to_world():
    assert client.get("/api/greeting").json() == {"message": "Hello, world!"}


def test_unknown_route_returns_404():
    assert client.get("/nope").status_code == 404
