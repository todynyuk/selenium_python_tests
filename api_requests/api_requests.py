import requests
import json

from utils.json_utils import write_response_to_file

base_url = "https://reqres.in/"
FILE_PATH = "/Users/tarasodynyuk/PycharmProjects/web_tests/resources/api/"


class ReqresInApi:

    @staticmethod
    def get_list_users():
        endpoint = "api/users?page=2"
        get_url = base_url + endpoint
        json_rs_path = f"{FILE_PATH}get/rs.json"
        response = requests.get(get_url)
        response_json = json.loads(response.text)
        write_response_to_file(json_rs_path, response_json)
        return response

    @staticmethod
    def get_single_user(user_id):
        endpoint = f"api/users/{user_id}"
        get_url = base_url + endpoint
        json_rs_path = f"{FILE_PATH}get/rs.json"
        response = requests.get(get_url)
        response_json = json.loads(response.text)
        write_response_to_file(json_rs_path, response_json)
        return response

    @staticmethod
    def create_new_user(user_name, user_job):
        json_rs_path = f"{FILE_PATH}post/rs.json"
        endpoint = "api/users"
        json_body = {
            "name": f"{user_name}",
            "job": f"{user_job}"
        }
        post_url = base_url + endpoint
        response = requests.post(post_url, json_body)
        res_json = json.loads(response.text)
        write_response_to_file(json_rs_path, res_json)
        return response

    @staticmethod
    def update_user(user_name, user_job, user_id):
        json_rs_path = f"{FILE_PATH}put/rs.json"
        endpoint = f"api/users/{user_id}"
        json_body = {
            "name": f"{user_name}",
            "job": f"{user_job}"
        }
        put_url = base_url + endpoint
        response = requests.put(put_url, json_body)
        res_json = json.loads(response.text)
        write_response_to_file(json_rs_path, res_json)
        return response

    @staticmethod
    def delete_user(user_id):
        endpoint = f"api/users/{user_id}"
        delete_url = base_url + endpoint
        response = requests.delete(delete_url)
        return response

    @staticmethod
    def register(email, password):
        json_rs_path = f"{FILE_PATH}post/rs.json"
        endpoint = "api/register"
        json_body = {
            "email": f"{email}",
            "password": f"{password}"
        }
        post_url = base_url + endpoint
        response = requests.post(post_url, json_body)
        res_json = json.loads(response.text)
        write_response_to_file(json_rs_path, res_json)
        return response

    @staticmethod
    def login(email, password):
        json_rs_path = f"{FILE_PATH}post/rs.json"
        endpoint = "api/login"
        json_body = {
            "email": f"{email}",
            "password": f"{password}"
        }
        post_url = base_url + endpoint
        response = requests.post(post_url, json_body)
        res_json = json.loads(response.text)
        write_response_to_file(json_rs_path, res_json)
        return response
