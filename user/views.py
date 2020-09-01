from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from . import serializer as user_serializer


class Authenticate(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = user_serializer.AuthenticationSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    serializer_class = user_serializer.UserSerializer

    def get_queryset(self):
        return User.objects.all()