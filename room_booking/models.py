from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Room(BaseModel):
    """
    Room Model
    """

    room_number = models.CharField(max_length=3)
    room_name = models.CharField(max_length=55)
    room_price = models.FloatField()
    room_capacity = models.IntegerField()

    objects = models.Manager()

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        unique_together = ("room_number", "room_name")


class Order(BaseModel):
    """
    Order Model
    """

    order_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="orders")
    order_start_date = models.DateField()
    order_end_date = models.DateField()

    objects = models.Manager()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
