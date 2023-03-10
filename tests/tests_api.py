import jsonpath as jsonpath
import pytest
import logging
from pytest_zebrunner import attach_test_artifact, attach_test_screenshot
import pyscreenrec
from utils.attachments import attach_screenshot, attach_logs, attach_recorded_video
import json
import os
import requests
import uuid

from utils.json_utils import change_json_values, write_response_to_file


class Test_API:

    def test_request_response(self):
        response = requests.get('https://solvdinternal.zebrunner.com')
        assert response.ok

    # url = "https://reqres.in/api/users"

    def test_create_task(self):
        payload = self.new_task_payload()
        create_task_response = self.create_task(payload)
        assert create_task_response.status_code == 200

        data = create_task_response.json()

        task_id = data["task"]["task_id"]
        get_task_response = self.get_task(task_id)
        assert get_task_response.status_code == 200
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == payload["content"]
        assert get_task_data["user_id"] == payload["user_id"]

    def test_update_task(self):
        payload = self.new_task_payload()
        create_task_response = self.create_task(payload)
        assert create_task_response.status_code == 200
        task_id = create_task_response.json()["task"]["task_id"]
        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my updated content",
            "is done": True
        }
        update_task_response = self.update_task(new_payload)
        assert update_task_response.status_code == 200
        get_task_response = self.get_task(task_id)
        assert get_task_response.status_code == 200
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["user_id"] == new_payload["user_id"]

    def test_list_tasks(self):
        count = 3
        payload = self.new_task_payload()
        for i in range(count):
            create_task_response = self.create_task(payload)
            assert create_task_response.status_code == 200
        user_id = payload["user_id"]
        list_task_response = self.list_tasks(user_id)
        assert list_task_response.status_code == 200
        data = list_task_response.json()
        tasks = data["tasks"]
        assert len(tasks) == count

    def test_delete_task(self):
        payload = self.new_task_payload()
        create_task_response = self.create_task(payload)
        assert create_task_response.status_code == 200
        task_id = create_task_response.json()["task"]["task_id"]
        delete_task_response = self.delete_task(task_id)
        assert delete_task_response.status_code == 200
        get_task_response = self.get_task(task_id)
        assert get_task_response.status_code == 404

    # UTIL METHODS--------------------------------------------------------------------------------------
    def create_task(self, payload):
        return requests.put("https://todo.pixegami.io/create-task", json=payload)

    def update_task(self, payload):
        return requests.put("https://todo.pixegami.io/update-task", json=payload)

    def get_task(self, task_id):
        return requests.get(f"https://todo.pixegami.io/get-task/{task_id}")

    def list_tasks(self, user_id):
        return requests.get(f"https://todo.pixegami.io/list-tasks/{user_id}")

    def delete_task(self, task_id):
        return requests.delete(f"https://todo.pixegami.io/delete-task/{task_id}")

    def new_task_payload(self):
        user_id = f"test user_{uuid.uuid4().hex}"
        content = f"test_content_{uuid.uuid4().hex}"
        return {
            "content": content,
            "user_id": user_id,
            "is_done": False
        }

    parameters = [("Test_User1", "programmer"), ("Test_User5", "designer"), ("Another_User", "HR")]

    @pytest.mark.parametrize("name,job", parameters)
    def test_create_user_post(self, name, job):
        url = "https://reqres.in/api/users"
        json_rq_path = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/post/rq.json"
        json_rs_path = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/post/rs.json"
        change_json_values(json_rq_path, name, job)
        file = open(json_rq_path, 'r')
        request_json = json.loads(file.read())
        response_json = requests.post(url, request_json)
        assert response_json.status_code == 201, "Status code not 201"
        res_json = json.loads(response_json.text)
        write_response_to_file(json_rs_path, res_json)
        file.close()

    parameters = [("Test_User1 Updated", "developer", 2), ("Test_User5 Updated", "game designer", 3),
                  ("Another_User Updated", "HR manager", 4)]

    @pytest.mark.parametrize("name,job,user_id", parameters)
    def test_update_user_put(self, name, job, user_id):
        url = f"https://reqres.in/api/users/{user_id}"
        json_rq_path = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/put/rq.json"
        json_rs_path = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/put/rs.json"
        change_json_values(json_rq_path, name, job)
        file = open(json_rq_path, 'r')
        request_json = json.loads(file.read())
        response_json = requests.put(url, request_json)
        assert response_json.status_code == 200, "Status code not 200"
        res_json = json.loads(response_json.text)
        write_response_to_file(json_rs_path, res_json)
        file.close()

    parameters = [("total", 1, 12), ("total_pages", 2, 2)]

    @pytest.mark.parametrize("param,page_number,expected_value", parameters)
    def test_get_user(self, param, page_number, expected_value):
        url = f"https://reqres.in/api/users?page={page_number}"
        json_rs_path = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/get/rs.json"
        response = requests.get(url)
        assert response.status_code == 200, "Status code not 200"
        response_json = json.loads(response.text)
        write_response_to_file(json_rs_path, response_json)
        pages = jsonpath.jsonpath(response_json, param)
        assert pages[0] == expected_value, "Values are not equals"

    parameters = [(2), (3)]

    @pytest.mark.parametrize("user_id", parameters)
    def test_delete_user(self, user_id):
        url = f"https://reqres.in/api/users/{user_id}"
        response = requests.delete(url)
        assert response.status_code == 204, "Status code not 204"


