from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

from user.models import User, Organisation


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
            # 'password': {'write_only': True},
            'last_login': {'write_only': True},
            'is_staff': {'write_only': True},
            'date_joined': {'write_only': True},
            'password_hint': {'write_only': True},
            'groups': {'write_only': True},
            'user_permissions': {'write_only': True},
            'is_superuser': {'write_only': True},
        }

    def validate(self, data):
        if data.get('password'):
            data['password'] = make_password(data['password'])
        return data

    # def create(self, validated_data):
    #     user = super(UserSerializer, self).create(validated_data)
    #     # user.set_password(validated_data['password'])
    #     # user.is_active = True
    #     # user.save()
    #     return user
    #
    # def update(self, instance, validated_data):
    #     user = super(UserSerializer, self).update(instance, validated_data)
    #     # if validated_data.get('password'):
    #     #     user.set_password(validated_data['password'])
    #     # user.save()
    #     return user


class UserUpdateSerializer(UserSerializer):
    password = serializers.CharField(required=False)


'''
pbkdf2_sha256$216000$AHaSXhA5r6SJ$NYAzUAYQSOpu/j9qnj/aVW0gbnqXNyGxtOMbpQ0jobY=
'''


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'
        read_only = ('created_at', 'updated_at')

