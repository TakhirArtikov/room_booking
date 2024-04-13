import pytest
from mixer.backend.django import mixer

from rest_framework.test import APIClient

from room_booking.serializers import User


@pytest.fixture()
def drf_client() -> APIClient:
    """Return APIClient instance"""
    return APIClient()


@pytest.fixture()
def logged_in_user(drf_client: APIClient, test_new_user: User):
    """Log in user"""

    drf_client.force_authenticate(test_new_user)
    return drf_client


@pytest.fixture()
def test_new_user() -> User:
    """New user"""
    user = mixer.blend(
        User,
        username="abc",
        email="abc@gmail.com",
    )
    user.set_password("123asdfg")
    user.save()
    return user
