from rest_framework.routers import DefaultRouter

from room_booking.views import RoomViewSet, OrderViewSet

router = DefaultRouter()
router.register("room", RoomViewSet, basename="room")
router.register("order", OrderViewSet, basename="order")

urlpatterns = []

urlpatterns += router.urls
