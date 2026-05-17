import pytest
from app import create_app
from app.services import user_service


@pytest.fixture
def client():
    app = create_app()
    user_service.users.clear()
    user_service.current_id = 1

    return app.test_client()


def test_user_flow(client):
    # Criar usuario
    response = client.post("/users", json={"name": "João"})
    assert response.status_code == 201

    user = response.get_json()
    user_id = user["id"]

    # Buscar usuario
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200

    # Atualizar usuario
    response = client.put(f"/users/{user_id}", json={"name": "Novo Nome"})
    assert response.status_code == 200
    assert response.get_json()["name"] == "Novo Nome"

    # Deletar usuario
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

    # Garantir que foi removido
    response = client.get(f"/users/{user_id}")
    assert response._status_code == 404


def test_list_users(client):
    client.post("/users", json={"name": "User1"})
    client.post("/users", json={"name": "User2"})

    response = client.get("/users")

    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 2


# 3 NOVOS TESTES


def test_update_user_functional(client):
    created = client.post("/users", json={"name": "Carlos"})
    user_id = created.get_json()["id"]

    response = client.put(f"/users/{user_id}", json={"name": "Carlos Silva"})

    assert response.status_code == 200
    assert response.get_json()["name"] == "Carlos Silva"


def test_delete_nonexistent_user_functional(client):
    response = client.delete("/users/999")

    assert response.status_code == 404


def test_get_nonexistent_user_functional(client):
    response = client.get("/users/999")

    assert response.status_code == 404
