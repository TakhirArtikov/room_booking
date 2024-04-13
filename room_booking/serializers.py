from typing import Any

from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers

from room_booking.models import Room, Order

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
        fields = ("id", "user", "order_number", "room_id", "order_start_date", "order_end_date", "room",)

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        start_date = attrs.get("order_start_date")
        end_date = attrs.get("order_end_date")
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("Start date must be before end date !")

        room_id = attrs.get("room_id")
        if Order.objects.filter(
                Q(order_end_date__gte=start_date, order_start_date__lte=start_date)
                | Q(order_end_date__gte=end_date, order_start_date__lte=end_date)
                | Q(order_start_date__gte=start_date, order_end_date__lte=end_date),
                room_id=room_id,
        ).exists():
            raise serializers.ValidationError(
                {
                    "room_id": "Room with this id already booked. Please try for different room_id."
                }
            )

        return attrs
