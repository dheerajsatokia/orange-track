from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import User


class AuthenticationSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        # token["type"] = user.type
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'last_login': {'write_only': True},
            'is_staff': {'write_only': True},
            'date_joined': {'write_only': True},
            'password_hint': {'write_only': True},
            'groups': {'write_only': True},
            'user_permissions': {'write_only': True},
            'is_superuser': {'write_only': True},
        }
