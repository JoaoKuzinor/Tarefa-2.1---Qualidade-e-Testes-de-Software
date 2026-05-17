import pytest
from app import create_app
from app.services import user_service


@pytest.fixture
def client():
    app = create_app()

    user_service.users.clear()
    user_service.current_id = 1

    return app.test_client()


def test_create_and_get_user(client):
    created = client.post("/users", json={"name": "João"})

    assert created.status_code == 201

    user_id = created.get_json()["id"]

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.get_json()["name"] == "João"


def test_create_and_update_user(client):
    created = client.post("/users", json={"name": "Maria"})

    user_id = created.get_json()["id"]

    response = client.put(f"/users/{user_id}", json={"name": "Maria Silva"})

    assert response.status_code == 200
    assert response.get_json()["name"] == "Maria Silva"


def test_create_and_delete_user(client):
    created = client.post("/users", json={"name": "Carlos"})

    user_id = created.get_json()["id"]

    deleted = client.delete(f"/users/{user_id}")

    assert deleted.status_code == 204

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 404


def test_duplicate_user_integration(client):
    client.post("/users", json={"name": "Ana"})

    response = client.post("/users", json={"name": "Ana"})

    assert response.status_code == 400


def test_update_nonexistent_user(client):
    response = client.put("/users/999", json={"name": "Teste"})

    assert response.status_code == 404
