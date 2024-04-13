from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "password2")

    def validate(self, attrs):
        if attrs.get("password") != attrs.pop("password2"):
            raise serializers.ValidationError({"password": _("Passwords must match")})

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class SignInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "password")

    def validate(self, attrs):
        user = auth.authenticate(email=attrs["email"], password=attrs["password"])
        if not user:
            raise AuthenticationFailed(_("Invalid credentials, try again"))
        if not user.is_active:
            raise AuthenticationFailed(_("Account disabled, contact admin"))
        return attrs
