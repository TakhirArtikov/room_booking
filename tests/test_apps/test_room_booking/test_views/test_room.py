import pytest
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from room_booking.models import Room


@pytest.mark.django_db()
def test_list(drf_client: APIClient, new_room: Room):  # pylint: disable=unused-argument
    """Testing list endpoint"""

    response = drf_client.get(path=reverse("room-list"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) != 0
