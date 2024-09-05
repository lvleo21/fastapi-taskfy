from fastapi.testclient import TestClient


def test_list_all_tasks_status_200(client: TestClient):
    response = client.get("/tasks")
    assert response.status_code == 200


def test_create_task_status_201(client: TestClient):

    task = {"title": "Título", "description": "Descrição", "completed": True}

    response = client.post("/tasks", json=task)
    assert response.status_code == 201


def test_create_task_response_has_id(client: TestClient):

    task = {"title": "Título", "description": "Descrição", "completed": True}

    response = client.post("/tasks", json=task)
    response_data = response.json()
    assert "id" in response_data


def test_create_task_response_is_same_with_payload(client: TestClient):
    payload = {"title": "Título", "description": "Descrição", "completed": True}

    response = client.post("/tasks", json=payload)
    response_data = response.json()
    del response_data["id"]
    assert payload == response_data


def test_create_task_status_422_with_error_on_title_maxlenght(client: TestClient):
    payload = {
        "title": "Meu título gigante co mmais de 15 caracteres",
        "description": "Descrição",
        "completed": True,
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 422


def test_create_task_response_body_with_error_on_title_maxlenght(
    client: TestClient,
):
    payload = {
        "title": "Títulooooooooooooooooooooooooooooooooooooooooooooooooooooo",
        "description": "Descrição",
        "completed": True,
    }
    response = client.post("/tasks", json=payload)
    assert response.json()["detail"][0]["loc"] == ["body", "title"]


def test_create_task_status_422_with_error_on_description_maxlenght(
    client: TestClient,
):
    payload = {
        "title": "Título",
        "description": "Minha descrição gigante com mais de 30 caracteres",
        "completed": True,
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 422


def test_create_task_response_body_with_error_on_description_maxlenght(
    client: TestClient,
):
    payload = {
        "title": "Título",
        "description": "Descriçãoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "completed": True,
    }
    response = client.post("/tasks", json=payload)
    assert response.json()["detail"][0]["loc"] == ["body", "description"]


def test_create_task_status_422_with_error_on_title_minlenght(client: TestClient):
    payload = {
        "title": "Me",
        "description": "Descrição",
        "completed": True,
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 422


def test_create_task_response_body_with_error_on_title_minlenght(
    client: TestClient,
):
    payload = {
        "title": "Tí",
        "description": "Descrição",
        "completed": True,
    }
    response = client.post("/tasks", json=payload)
    assert response.json()["detail"][0]["loc"] == ["body", "title"]


def test_create_task_status_422_with_error_on_description_minlenght(
    client: TestClient,
):
    payload = {
        "title": "Título",
        "description": "Mi",
        "completed": True,
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 422


def test_create_task_response_body_with_error_on_description_minlenght(
    client: TestClient,
):
    payload = {
        "title": "Título",
        "description": "De",
        "completed": True,
    }
    response = client.post("/tasks", json=payload)
    assert response.json()["detail"][0]["loc"] == ["body", "description"]


def test_create_task_status_422_with_error_on_completed_invalid_value(
    client: TestClient,
):
    payload = {
        "title": "Título",
        "description": "Descrição",
        "completed": "Joana",
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 422


def test_create_task_response_body_with_error_on_completed_invalid_value(
    client: TestClient,
):
    payload = {
        "title": "Título",
        "description": "Descrição",
        "completed": "Joana",
    }
    response = client.post("/tasks", json=payload)
    assert response.json()["detail"][0]["loc"] == ["body", "completed"]


def test_put_task_status_201(client: TestClient):
    task = {"title": "Título", "description": "Descrição", "completed": True}
    response = client.post("/tasks", json=task)
    task_id = response.json()["id"]

    updated_task = {
        "title": "New Título",
        "description": "New Descrição",
        "completed": False,
    }
    response = client.put(f"/tasks/{task_id}", json=updated_task)
    assert response.status_code == 200


def test_delete_task_status_201(client: TestClient):
    task = {"title": "Título", "description": "Descrição", "completed": True}
    response = client.post("/tasks", json=task)
    task_id = response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200


def test_delete_task_return_status_404_if_task_removed(client: TestClient):
    task = {"title": "Título", "description": "Descrição", "completed": True}
    response = client.post("/tasks", json=task)
    task_id = response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
