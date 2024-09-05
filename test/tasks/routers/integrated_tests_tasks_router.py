from tests import NEW_TASK, EDIT_TASK, client, database_test, create_task

def test_less_than_the_limit_title():
    new_task = NEW_TASK.copy()
    new_task["title"] = "A"

    response = client.post('/tasks', json=new_task)

    assert response.status_code == 422

def test_exception_limit_title():
    new_task = NEW_TASK.copy()
    new_task["title"] = "T"*121

    response = client.post('/tasks', json=new_task)

    assert response.status_code == 422

def test_less_than_the_limit_description():
    new_task = NEW_TASK.copy()
    new_task["description"] = "A"

    response = client.post('/tasks', json=new_task)

    assert response.status_code == 422

def test_exception_limit_description():
    new_task = NEW_TASK.copy()
    new_task["description"] = "T"*121

    response = client.post('/tasks', json=new_task)

    assert response.status_code == 422

def test_no_boolean_in_completed():
    response_create = create_task()
    task_id = response_create.json()["id"]

    completed_task = {
        "completed": "Test"
    }

    response = client.patch(f'/tasks/{task_id}', json=completed_task)

    assert response.status_code == 422

def test_return_not_found_of_id_not_found():
    database_test()

    response_get = client.get("/tasks/100")

    response_get.status_code == 404

def test_return_not_found_of_id_not_found_in_put():
    database_test()

    edited_task = EDIT_TASK

    response_put = client.put(f'/tasks/100', json=edited_task)

    response_put.status_code == 404

def test_return_not_found_of_id_not_found_in_patch():
    database_test()

    completed_task = {
        "completed": "Test"
    }

    response_patch = client.patch(f'/tasks/100', json=completed_task)

    response_patch.status_code == 404

def test_return_not_found_of_id_not_found_in_patch():
    database_test()

    response_delete = client.delete(f'/tasks/100')

    response_delete.status_code == 404
