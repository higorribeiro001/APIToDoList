from tests import NEW_TASK, EDIT_TASK, client, database_test, create_task

def test_create_task():
    response = create_task()

    new_task_copy = NEW_TASK.copy()
    new_task_copy["id"] = response.json()["id"]
    new_task_copy["completed"] = False

    assert response.status_code == 201
    assert response.json() == new_task_copy

def test_list_tasks():
    database_test()
    response = client.get('/tasks')

    assert response.status_code == 200

def test_find_by_id():
    response = create_task()

    task_id = response.json()["id"]

    response_get = client.get(f'/tasks/{task_id}')

    assert response_get.status_code == 200
	
def test_update_task():
    response_create = create_task()

    edited_task = EDIT_TASK
    task_id = response_create.json()["id"]

    response_put = client.put(f'/tasks/{task_id}', json=edited_task)

    edited_task["id"] = task_id

    assert response_put.status_code == 200
    assert response_put.json() == edited_task

def test_completed_task():
    response_create = create_task()

    completed_task = {
          "completed": True
    }
    task_id = response_create.json()["id"]

    response_patch = client.patch(f'/tasks/{task_id}', json=completed_task)

    completed_task = NEW_TASK.copy()
    completed_task["id"] = task_id
    completed_task["completed"] = True

    assert response_patch.status_code == 200
    assert response_patch.json() == completed_task

def test_delete_task():
    response_create = create_task()
    task_id = response_create.json()["id"]

    response_delete = client.delete(f'/tasks/{task_id}')

    assert response_delete.status_code == 204