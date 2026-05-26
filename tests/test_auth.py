from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "username": "lu",
            "email": "lu@example.com",
            "password": "12345678"
        },
    )
    assert response.status_code == 201
    body = response.json()
    assert body["message"] == "registration endpoint created"
    assert body["user"]["username"] == "lu"
    assert body["user"]["email"] == "lu@example.com"
