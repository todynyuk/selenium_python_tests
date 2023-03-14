from api_methods.api_methods import new_task_payload, create_task, get_task, update_task, list_tasks, delete_task
import requests
import logging

logger = logging.getLogger("api")
URL = "https://todo.pixegami.io/"


class Test_API:

    def test_request_response(self):
        response = requests.get('https://solvdinternal.zebrunner.com')
        assert response.ok

    def test_create_task(self):
        payload = new_task_payload(self)
        create_task_response = create_task(self, payload, URL)
        assert create_task_response.status_code == 200

        data = create_task_response.json()

        task_id = data["task"]["task_id"]
        get_task_response = get_task(self, task_id, URL)
        assert get_task_response.status_code == 200
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == payload["content"]
        assert get_task_data["user_id"] == payload["user_id"]

    def test_update_task(self):
        payload = new_task_payload(self)
        create_task_response = create_task(self, payload, URL)
        assert create_task_response.status_code == 200
        task_id = create_task_response.json()["task"]["task_id"]
        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my updated content",
            "is done": True
        }
        update_task_response = update_task(self, new_payload, URL)
        assert update_task_response.status_code == 200
        get_task_response = get_task(self, task_id, URL)
        assert get_task_response.status_code == 200
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["user_id"] == new_payload["user_id"]

    def test_list_tasks(self):
        count = 3
        payload = new_task_payload(self)
        for i in range(count):
            create_task_response = create_task(self, payload, URL)
            assert create_task_response.status_code == 200
        user_id = payload["user_id"]
        list_task_response = list_tasks(self, user_id, URL)
        assert list_task_response.status_code == 200
        data = list_task_response.json()
        tasks = data["tasks"]
        assert len(tasks) == count

    def test_delete_task(self):
        payload = new_task_payload(self)
        create_task_response = create_task(self, payload, URL)
        assert create_task_response.status_code == 200
        task_id = create_task_response.json()["task"]["task_id"]
        delete_task_response = delete_task(self, task_id, URL)
        assert delete_task_response.status_code == 200
        get_task_response = get_task(self, task_id, URL)
        assert get_task_response.status_code == 404
