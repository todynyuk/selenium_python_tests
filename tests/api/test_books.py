import json

from api_requests.api_books_requests import get_books, get_book


class TestBooks:

    def test_get_books_200(self):
        response = get_books()
        assert response.status_code == 200, 'Status code is not ok'

    def test_get_books_invalid_type(self):
        response = get_books(book_type='a1b2c0')
        assert response.status_code == 400, f'Actual status code is incorrect.' \
                                            f' Expected: 400, Actual: {self.response.status_code}'
        assert response.json()['error'] == "Invalid value for query parameter 'type'." \
                                           " Must be one of: fiction, non-fiction.", 'Response message is not correct'

    def test_get_books_limit_greater_than_20(self):
        response = get_books(limit=21)
        assert response.status_code == 400, f'Actual status code is incorrect.' \
                                            f' Expected: 400, Actual: {self.response.status_code}'
        assert response.json()['error'] == "Invalid value for query parameter 'limit'." \
                                           " Cannot be greater than 20.", 'Response message is not correct'

    def test_get_books_when_negative_limit(self):
        response = get_books(limit=-5)
        assert response.status_code == 400, f'Actual status code is incorrect.' \
                                            f' Expected: 400, Actual: {self.response.status_code}'
        assert response.json()['error'] == "Invalid value for query parameter 'limit'." \
                                           " Must be greater than 0.", 'Response message is not correct'

    def test_get_books_when_limit_is_0(self):
        response = get_books(limit=0)
        assert response.status_code == 200, f'Actual status code is incorrect.' \
                                            f' Expected: 200, Actual: {self.response.status_code}'
        assert len(response.json()) == 6, 'Total books returned is incorrect'

    def test_get_all_books(self):
        response = get_books(limit=6)
        assert len(response.json()) == 6, 'Total books returned is incorrect'

    def test_verify_books_attributes(self):
        response = get_books()
        rez = response.json()
        result = list(rez[0].keys())

        for item in list((response.json()[0]).keys()):
            assert item in result == ['id', 'name', 'type', 'available'], "Attribute doesn't exist"

    def test_get_book(self):
        response = get_book(3)
        expected = {"id": 3,
                    "name": "The Vanishing Half",
                    "author": "Brit Bennett",
                    "type": "fiction",
                    "price": 16.2,
                    "current-stock": 987,
                    "available": True}
        assert response.status_code == 200, f'Actual status code is incorrect.' \
                                            f' Expected: 200, Actual: {self.response.status_code}'
        assert response.json() == expected, 'Response body is incorrect'

    def test_get_book_invalid_id(self):
        response = get_book(87524)
        assert response.status_code == 404, f'Actual status code is incorrect.' \
                                            f' Expected: 404, Actual: {self.response.status_code}'
        assert response.json()['error'] == "No book with id 87524", 'Wrong message error was returned'
