from django.contrib import admin

from room_booking.models import Room, Order
from .forms import OrderBookingForm


@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ("id", "room_name", "room_number", "room_price", "room_capacity")
    ordering = ("room_price", "room_capacity")
    list_display_links = ("id", "room_name")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "room", "order_start_date", "order_end_date")
    ordering = ("order_start_date", "order_end_date")
    form = OrderBookingForm
