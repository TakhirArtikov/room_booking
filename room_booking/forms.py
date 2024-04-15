from django import forms

from room_booking.exceptions import RoomBookedException, InvalidBookingDatesException
from room_booking.models import Order
from room_booking.util import room_booking_validation


class OrderBookingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "order_number",
            "order_start_date",
            "order_end_date",
            "room",
        ]

    def clean(self):
        cleaned_data = super().clean()
        try:
            room_booking_validation(cleaned_data)
        except (RoomBookedException, InvalidBookingDatesException, Exception) as e:
            raise forms.ValidationError(e)

        return cleaned_data
