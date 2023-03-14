import requests
import logging
from utils.json_utils import change_json_values, write_response_to_file
import json
import jsonpath as jsonpath
import pytest

URL = "https://reqres.in/api/users"
FILE_PATH = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/"
logger = logging.getLogger("api")


class Test_Reqres_API:
    parameters = [("Test_User1", "programmer"), ("Test_User5", "designer"), ("Another_User", "HR")]

    @pytest.mark.parametrize("name,job", parameters)
    def test_create_user_post(self, name, job):
        json_rq_path = f"{FILE_PATH}post/rq.json"
        json_rs_path = f"{FILE_PATH}post/rs.json"
        change_json_values(json_rq_path, name, job)
        file = open(json_rq_path, 'r')
        request_json = json.loads(file.read())
        response_json = requests.post(URL, request_json)
        assert response_json.status_code == 201, "Status code not 201"
        res_json = json.loads(response_json.text)
        write_response_to_file(json_rs_path, res_json)
        file.close()
        get_task_data = response_json.json()
        assert get_task_data["name"] == name
        assert get_task_data["job"] == job

    parameters = [("Test_User1 Updated", "developer", 2), ("Test_User5 Updated", "game designer", 3),
                  ("Another_User Updated", "HR manager", 4)]

    @pytest.mark.parametrize("name,job,user_id", parameters)
    def test_update_user_put(self, name, job, user_id):
        url = f"{URL}/{user_id}"
        json_rq_path = f"{FILE_PATH}put/rq.json"
        json_rs_path = f"{FILE_PATH}put/rs.json"
        change_json_values(json_rq_path, name, job)
        file = open(json_rq_path, 'r')
        request_json = json.loads(file.read())
        response_json = requests.put(url, request_json)
        assert response_json.status_code == 200, "Status code not 200"
        res_json = json.loads(response_json.text)
        write_response_to_file(json_rs_path, res_json)
        file.close()
        get_task_data = response_json.json()
        assert get_task_data["name"] == name
        assert get_task_data["job"] == job

    parameters = [("total", 1, 12), ("total_pages", 2, 2)]

    @pytest.mark.parametrize("param,page_number,expected_value", parameters)
    def test_get_user(self, param, page_number, expected_value):
        url = f"{URL}?page={page_number}"
        json_rs_path = f"{FILE_PATH}get/rs.json"
        response = requests.get(url)
        assert response.status_code == 200, "Status code not 200"
        response_json = json.loads(response.text)
        write_response_to_file(json_rs_path, response_json)
        pages = jsonpath.jsonpath(response_json, param)
        assert pages[0] == expected_value, "Values are not equals"

    parameters = [(2), (3)]

    @pytest.mark.parametrize("user_id", parameters)
    def test_delete_user(self, user_id):
        url = f"{URL}/{user_id}"
        response = requests.delete(url)
        assert response.status_code == 204, "Status code not 204"
