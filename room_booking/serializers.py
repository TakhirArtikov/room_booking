from typing import Any

from django.contrib.auth import get_user_model
from rest_framework import serializers

from room_booking.exceptions import InvalidBookingDatesException, RoomBookedException
from room_booking.models import Room, Order
from room_booking.util import room_booking_validation

User = get_user_model()


class RoomSerializer(serializers.ModelSerializer):
    """
    Serializer for Room model
    """

    class Meta:
        model = Room
        fields = ("id", "room_name", "room_price", "room_number", "room_capacity")


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order objects
    """

    room = RoomSerializer(read_only=True)
    room_id = serializers.IntegerField(write_only=True)
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), queryset=User.objects.all()
    )

    class Meta:
        """
        Config for order objects
        """

        model = Order
        fields = (
            "id",
            "user",
            "order_number",
            "room_id",
            "order_start_date",
            "order_end_date",
            "room",
        )

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        try:
            room_booking_validation(attrs)
        except (RoomBookedException, InvalidBookingDatesException) as e:
            raise serializers.ValidationError(e)

        return attrs
