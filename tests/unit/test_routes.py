import pytest
from app import create_app

# def test_health_check():
#     app = create_app()
#     client = app.test_client()

#     response = client.get("/status")

#     assert response.status_code == 200
#     assert response.get_json() == {"status": "ok"}


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()


from app.services import user_service


@pytest.fixture(autouse=True)
def reset_users():
    user_service.users.clear()
    user_service.current_id = 1


def test_create_user_sucess(client):
    response = client.post("/users", json={"name": "João"})

    assert response.status_code == 201
    assert response.get_json()["name"] == "João"


def test_create_user_without_name(client):
    response = client.post("/users", json={})

    assert response.status_code == 400
    assert "name is required" in str(response.data)


def test_get_user(client):
    client.post("/users", json={"name": "Teste"})

    response = client.get("/users/1")

    assert response.status_code == 200


def test_get_user_not_found(client):
    response = client.get("/users/999")

    assert response.status_code == 404
    assert "User not found" in str(response.data)


def test_delete_user(client):
    client.post("/users", json={"name": "Delete"})

    response = client.delete("/users/1")

    assert response.status_code == 204


def test_update_user_success(client):
    # 1. Criar usuário
    response = client.post("/users", json={"name": "João"})
    assert response.status_code == 201

    user_id = response.get_json()["id"]

    # 2. Atualizar usuário
    response = client.put(f"/users/{user_id}", json={"name": "Novo Nome"})

    assert response.status_code == 200
    assert response.get_json()["name"] == "Novo Nome"


def test_should_not_allow_duplicate_users():
    from app.services import user_service

    user_service.users.clear()
    user_service.current_id = 1

    user_service.create_user({"name": "João"})

    user = user_service.create_user({"name": "João"})

    assert user is None


def test_should_return_400_when_user_already_exists(client):
    client.post("/users", json={"name": "João"})

    response = client.post("/users", json={"name": "João"})

    assert response.status_code == 400


# NOVOS TESTES UNITARIOS


def test_create_multiple_users(client):
    response1 = client.post("/users", json={"name": "João"})
    response2 = client.post("/users", json={"name": "Maria"})

    assert response1.status_code == 201
    assert response2.status_code == 201


def test_users_should_have_different_ids(client):
    response1 = client.post("/users", json={"name": "João"})
    response2 = client.post("/users", json={"name": "Maria"})

    id1 = response1.get_json()["id"]
    id2 = response2.get_json()["id"]

    assert id1 != id2


def test_update_user_without_name(client):
    response = client.post("/users", json={"name": "João"})
    user_id = response.get_json()["id"]

    response = client.put(f"/users/{user_id}", json={})

    assert response.status_code == 400


# def test_update_user_with_empty_name(client):
#     response = client.post("/users", json={"name": "João"})
#     user_id = response.get_json()["id"]

#     response = client.put(f"/users/{user_id}", json={"name": ""})

#     assert response.status_code == 400


def test_deleted_user_should_not_be_found(client):
    response = client.post("/users", json={"name": "Delete"})
    user_id = response.get_json()["id"]

    client.delete(f"/users/{user_id}")

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 404


def test_create_user_returns_json(client):
    response = client.post("/users", json={"name": "João"})

    assert response.content_type == "application/json"


def test_get_user_returns_correct_name(client):
    client.post("/users", json={"name": "Carlos"})

    response = client.get("/users/1")

    assert response.get_json()["name"] == "Carlos"


def test_route_not_allowed(client):
    response = client.patch("/users/1")

    assert response.status_code in [400, 405]
