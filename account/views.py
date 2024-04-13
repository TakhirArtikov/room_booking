from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from account.serializer import SignUpSerializer, SignInSerializer


# Create your views here.


class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
