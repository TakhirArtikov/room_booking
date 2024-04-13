from django.urls import path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from account.views import SignUpAPIView

app_name = "account"

router = routers.DefaultRouter()

urlpatterns = [
    path("sign_in/", TokenObtainPairView.as_view(), name="sign_in"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("sign_up/", SignUpAPIView.as_view(), name="sign_up"),
]

urlpatterns += router.urls
