import datetime

import pytest

from mixer.backend.django import mixer

from room_booking.models import Order


@pytest.fixture()
def new_order(test_new_user, new_room) -> Order:
    """Create a new order for test"""

    order = mixer.blend(
        Order,
        user=test_new_user,
        order_number=2,
        room_id=new_room.id,
        order_start_date=datetime.date(2024, 5, 28),
        order_end_date=datetime.date(2024, 5, 30),
    )
    return order
