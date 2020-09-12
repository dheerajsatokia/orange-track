from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from .models import Organisation
from . import models
from . import serializer as user_serializer
from .serializer import UserOrganisationSerializer
from .models import User
from OrangeTrackBackend.constants import user_constants


class Authenticate(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = user_serializer.AuthenticationSerializer


# {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action in ['put', 'patch']:
            return user_serializer.UserUpdateSerializer
        else:
            return user_serializer.UserSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = user_serializer.OrganisationSerializer

    def get_queryset(self):
        if self.request.user.user_type == user_constants.SUPER_ADMIN:
            return models.Organisation.objects.all()
        elif self.request.user.user_type == user_constants.ADMIN:
            return models.Organisation.objects \
                .select_related('admin') \
                .filter(user=self.request.user)


class Assign(APIView):
    serializer_class = UserOrganisationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return models.UserOrganisation.objects.create()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
