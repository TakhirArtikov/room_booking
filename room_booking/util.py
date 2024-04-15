from typing import Any

from django.db.models import Q

from room_booking.exceptions import InvalidBookingDatesException, RoomBookedException
from room_booking.models import Order


def room_booking_validation(attrs: dict[str, Any]) -> dict[str, Any]:
    """
    Validate the attributes of the order_start_date, and order_end_date
    Validate the attribute of the order booking room
    Required attributes: order_start_date, order_end_date, room
    :param attrs:
    :return:
    """
    start_date = attrs.get("order_start_date")
    end_date = attrs.get("order_end_date")
    if start_date and end_date and start_date > end_date:
        raise InvalidBookingDatesException

    room = attrs.get("room")
    print(room)
    if Order.objects.filter(
        Q(order_end_date__gte=start_date, order_start_date__lte=start_date)
        | Q(order_end_date__gte=end_date, order_start_date__lte=end_date)
        | Q(order_start_date__gte=start_date, order_end_date__lte=end_date),
        room=room,
    ).exists():
        raise RoomBookedException

    return attrs
