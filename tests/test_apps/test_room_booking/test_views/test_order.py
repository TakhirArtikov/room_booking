import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from room_booking.models import Order, Room

User = get_user_model()


@pytest.mark.django_db()
def test_list(
    logged_in_user: APIClient, new_order: Order  # pylint: disable=unused-argument
):
    """Testing order list endpoint"""

    response = logged_in_user.get(path=reverse("order-list"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) != 0


@pytest.mark.django_db()
def test_add_order(logged_in_user: APIClient, test_new_user: User, new_room: Room):
    """Testing order create endpoint"""

    response = logged_in_user.post(
        path=reverse("order-list"),
        data={
            "user": test_new_user.id,
            "order_number": 2,
            "room_id": new_room.id,
            "order_start_date": "2024-04-13",
            "order_end_date": "2024-04-13",
        },
    )

    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert Order.objects.filter(id=response_data.get("id")).exists()
    assert test_new_user.id == response_data.get("user")
