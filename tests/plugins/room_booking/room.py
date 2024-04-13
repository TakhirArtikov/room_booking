import pytest

from mixer.backend.django import mixer

from room_booking.models import Room


@pytest.fixture()
def new_room() -> Room:
    """Create a new room for test"""

    return mixer.blend(
        Room,
        room_number="4",
        room_name="A",
        room_price=15,
        room_capacity=2,
    )
