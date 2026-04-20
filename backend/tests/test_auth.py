def test_register_success(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "user@melodia.com",
            "username": "testuser",
            "password": "secret123",
            "role": "listener",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "user@melodia.com"
    assert data["role"] == "listener"
    assert "hashed_password" not in data


def test_register_duplicate_email(client):
    payload = {
        "email": "user@melodia.com",
        "username": "testuser",
        "password": "secret123",
        "role": "listener",
    }
    client.post("/auth/register", json=payload)
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_login_success(client):
    client.post(
        "/auth/register",
        json={
            "email": "user@melodia.com",
            "username": "testuser",
            "password": "secret123",
            "role": "listener",
        },
    )
    response = client.post(
        "/auth/login",
        json={"email": "user@melodia.com", "password": "secret123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post(
        "/auth/register",
        json={
            "email": "user@melodia.com",
            "username": "testuser",
            "password": "secret123",
            "role": "listener",
        },
    )
    response = client.post(
        "/auth/login",
        json={"email": "user@melodia.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401


def test_me_success(client):
    client.post(
        "/auth/register",
        json={
            "email": "user@melodia.com",
            "username": "testuser",
            "password": "secret123",
            "role": "listener",
        },
    )
    login = client.post(
        "/auth/login",
        json={"email": "user@melodia.com", "password": "secret123"},
    )
    token = login.json()["access_token"]
    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "user@melodia.com"


def test_me_without_token(client):
    response = client.get("/auth/me")
    assert response.status_code == 401
