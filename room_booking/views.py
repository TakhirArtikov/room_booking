from django.db.models import QuerySet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from room_booking import serializers
from room_booking.filters import RoomFilter
from room_booking.models import Order, Room


class RoomViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that allows Room to be viewed or edited
    """

    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["room_price", "room_capacity"]
    filterset_class = RoomFilter

    pagination_class = LimitOffsetPagination


class OrderViewSet(ModelViewSet):
    """
    API endpoint that allows orders to do CRUD operations
    """

    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self) -> QuerySet[Order]:
        return self.queryset.filter(user=self.request.user)
