from api_requests.api_clients_requests import get_token
from api_requests.api_orders_requests import add_order, edit_order, get_order, delete_order, get_orders


class TestOrders:
    def setup_method(self):
        self.token = get_token()

    def test_add_order_book_out_of_stock(self):
        response = add_order(self.token, 2, 'Test')
        assert response.status_code == 404, \
            f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
        assert response.json()['error'] == 'This book is not in stock. Try again later.', 'The error is incorrect'

    def test_add_valid_order(self):
        response = add_order(self.token, 1, 'Test')
        assert response.status_code == 201, \
            f"Error: status code is not correct. Expected: 201, Actual: {response.status_code}"
        assert response.json()['created'] is True, 'Order not created'
        delete_order(self.token, response.json()['orderId'])

    def test_get_orders(self):
        add1 = add_order(self.token, 1, 'user1')
        add2 = add_order(self.token, 4, 'user2')
        response = get_orders(self.token)
        assert response.status_code == 200, \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert len(response.json()) == 2, 'Total of orders returned is incorrect'
        delete_order(self.token, add1.json()['orderId'])
        delete_order(self.token, add2.json()['orderId'])

    def test_delete_order(self):
        add = add_order(self.token, 4, "Test")
        response = delete_order(self.token, add.json()['orderId'])
        assert response.status_code == 204, \
            f"Error: status code is not correct. Expected: 204, Actual: {response.status_code}"
        verify = get_orders(self.token)
        assert len(verify.json()) == 0, 'Order was not deleted'

    def test_get_one_order(self):
        order = add_order(self.token, 1, 'TesT').json()['orderId']
        response = get_order(self.token, order)
        assert response.status_code == 200, \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert response.json()['id'] == order, 'id is not OK'
        assert response.json()['bookId'] == 1, 'bookId is not OK'
        assert response.json()['customerName'] == 'TesT', 'customerName is not OK'
        assert response.json()['quantity'] == 1, 'quantity is not OK'
        delete_order(self.token, order)

    def test_delete_invalid_orderId(self):
        response = delete_order(self.token, 'querty5')
        assert response.status_code == 404, \
            f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
        assert response.json()['error'] == 'No order with id querty5.', 'The error returned is not correct'

    def test_get_order_invalid_id(self):
        response = get_order(self.token, 'e455e4')
        assert response.status_code == 404, \
            f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
        assert response.json()['error'] == 'No order with id e455e4.', 'The error returned is not correct'

    def test_edit_invalid_orderId(self):
        response = edit_order(self.token, '4d5y7r', 'Test')
        assert response.status_code == 404, \
            f"Error: status code is not correct. Expected: 404, Actual: {response.status_code}"
        assert response.json()['error'] == 'No order with id 4d5y7r.', 'The error returned is not correct'

    def test_edit_orderId(self):
        order = add_order(self.token, 1, 'Test_Order').json()['orderId']
        response = edit_order(self.token, order, 'Order_Test')
        assert response.status_code == 204, \
            f"Error: status code is not correct. Expected: 204, Actual: {response.status_code}"
        get = get_order(self.token, order)
        assert get.json()['customerName'] == 'Order_Test', 'Customer name was not updated'
        delete_order(self.token, order)
