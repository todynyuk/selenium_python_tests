from api_requests.api_requests import ReqresInApi
from api_validations.api_validations import Validations
import logging
import pytest

logger = logging.getLogger("api")

class Test_Reqres_Negative:
    parameters = [(25), (35)]

    @pytest.mark.parametrize("user_id", parameters)
    def test_get_invalid_single_user(self, user_id):
        response = ReqresInApi.get_single_user(user_id)
        assert Validations.valid_status_code(response, 404), \
            f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
        assert Validations.response_time(response, 800), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {800} ms."
        logger.info("Single user not found. Empty response.")

    parameters = [("", "ReqRes"), ("", "Curly")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_registration_without_email(self, username, password):
        response = ReqresInApi.register(username, password)
        assert Validations.valid_status_code(response, 400),\
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing email or username"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing email or username")

    parameters = [("janet.weaver@reqres.in", ""), ("emma.wong@reqres.in", "")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_registration_without_password(self, username, password):
        response = ReqresInApi.register(username, password)
        assert Validations.valid_status_code(response, 400),\
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing password"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing password")

    parameters = [("", "ReqRes"), ("", "Curly")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_login_without_email(self, username, password):
        response = ReqresInApi.login(username, password)
        assert Validations.valid_status_code(response, 400),\
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing email or username"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing email or username")

    parameters = [("janet.weaver@reqres.in", ""), ("emma.wong@reqres.in", "")]

    @pytest.mark.parametrize("username,password", parameters)
    def test_login_without_password(self, username, password):
        response = ReqresInApi.login(username, password)
        assert Validations.valid_status_code(response, 400),\
            f"Error: status code is not correct. Expected: 400, Actual: {response.status_code}"
        assert Validations.check_json_keys(response, ["error"]), \
            "The expected set of keys does not match the actual one."
        assert Validations.check_json_values(response, ["Missing password"]), \
            "The expected values do not match the actual one."
        assert Validations.response_time(response, 8000), \
            f"Response time({round(response.elapsed.total_seconds() * 1000)}) is more than {8000} ms."
        logger.info("Error: Missing password")