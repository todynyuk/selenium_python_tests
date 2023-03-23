import logging
import pytest

from utils.bookings import Bookings

from utils.http_manager import HttpManager

logger = logging.getLogger("api")


class Test_Booking_API_GetTests:

    def test_get_booking(self):
        response = HttpManager.get(Bookings.GET_BOOKING.format(Bookings.get_random_booking()))
        assert response.status_code == 200, \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert isinstance(response.json()['firstname'], str), "Isinstance is not str"
        assert isinstance(response.json()['depositpaid'], bool), "Isinstance is not bool"

    def test_get_booking_ids(self):
        response = HttpManager.get(Bookings.GET_BOOKINGS)
        assert response.status_code == 200, \
            f"Error: status code is not correct. Expected: 200, Actual: {response.status_code}"
        assert isinstance(response.json()[0]['bookingid'], int), "Isinstance is not int"
