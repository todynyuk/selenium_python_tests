import json
import logging

logger = logging.getLogger("api")


class Validations:

    @staticmethod
    def valid_status_code(response, status_code):
        return status_code == response.status_code

    @staticmethod
    def check_json_keys(response, expected_keys):
        response_keys = (json.loads(response.text)).keys()
        return list(response_keys) == expected_keys

    @staticmethod
    def check_json_values(response, expected_keys):
        response_values = (json.loads(response.text)).values()
        return expected_keys in list(response_values) or expected_keys == list(response_values)

    @staticmethod
    def response_time(response, expected_time):
        return round(response.elapsed.total_seconds() * 1000) < expected_time
