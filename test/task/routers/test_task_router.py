from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_list_all_tasks_status_200():
    response = client.get('/tasks')
    assert response.status_code == 200


def test_create_task_status_201():
    task = {
        'title': "Título",
        'description': "Descrição",
        'completed': True
    }

    response = client.post('/tasks', json=task)
    assert response.status_code == 201


def test_create_task_response_has_id():
    task = {
        'title': "Título",
        'description': "Descrição",
        'completed': True
    }

    response = client.post('/tasks', json=task)
    response_data = response.json()
    assert 'id' in response_data


def test_create_task_response_is_same_with_payload():
    payload = {
        'title': "Título",
        'description': "Descrição",
        'completed': True
    }

    response = client.post('/tasks', json=payload)
    response_data = response.json()
    del response_data['id']
    assert payload == response_data
