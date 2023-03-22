import pytest
import random

from api_requests.api_clients_requests import login


class TestApiClient:
    nr = random.randint(1, 9999999)
    clientName = 'Test3'
    clientEmail = f'test_mailtest3{nr}@mailinator.com'

    def setup_method(self):
        self.response = login(self.clientName, self.clientEmail)

    def test_successful_login(self):
        assert self.response.status_code == 201, f'Actual status code is incorrect. ' \
                                                 f'Expected: 400, Actual: {self.response.status_code}'
        assert 'accessToken' in self.response.json().keys(), 'Token property is not present in the response'

    def test_invalid_client_name(self):
        self.response = login("", "test@email.com")
        assert self.response.status_code == 400, f'Actual status code is incorrect.' \
                                                 f' Expected: 400, Actual: {self.response.status_code}'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    def test_invalid_login_credentials(self):
        self.response = login("3", "6")
        assert self.response.status_code == 400, f'Actual status code is incorrect.' \
                                                 f' Expected: 400, Actual: {self.response.status_code}'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    def test_missing_client_name(self):
        self.response = login("", "test@e.com")
        assert self.response.status_code == 400, f'Actual status code is incorrect.' \
                                                 f' Expected: 400, Actual: {self.response.status_code}'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    def test_invalid_email_test(self):
        self.response = login("test_", "test@domain")
        assert self.response.status_code == 400, f'Actual status code is incorrect.' \
                                                 f' Expected: 400, Actual: {self.response.status_code}'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'

    def test_missing_email(self):
        self.response = login("login4", "")
        assert self.response.status_code == 400, f'Actual status code is incorrect.' \
                                                 f' Expected: 400, Actual: {self.response.status_code}'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'

    def test_missing_login_credentials(self):
        self.response = login("", "")
        assert self.response.status_code == 400, f'Actual status code is incorrect.' \
                                                 f' Expected: 400, Actual: {self.response.status_code}'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    param = [
        ('', 'test@email.com'),
        ('return_eroare!', 't'),
        ('return_eroare!', 'test@email.com'),
        ('2', 'test.com'),
        ('tst', 'test.'),
        ('2', 'test.com'),
        (' ', 'test@domain'),
        ('!', 'test@')

    ]

    @pytest.mark.parametrize('username, user_email', param)
    def test_invalid_email_param(self, username, user_email):
        self.response = login("username", "user_email")
        assert self.response.status_code == 400, f'Actual status code is incorrect.' \
                                                 f' Expected: 400, Actual: {self.response.status_code}'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'
