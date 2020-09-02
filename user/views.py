from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializer as user_serializer
from .models import User


class Authenticate(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = user_serializer.AuthenticationSerializer


# {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)

    # serializer_class = user_serializer.UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action in ['put', 'patch']:
            return user_serializer.UserUpdateSerializer
        else:
            return user_serializer.UserSerializer
