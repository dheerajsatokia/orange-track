from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from project_management import serializer as project_serializer
from . import models
from OrangeTrackBackend.constants import user_constants
from project_management.models import ProjectUser
from rest_framework.response import Response
from rest_framework import status
from project_management.serializer import ProjectUserSerializer, ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        if self.request.user.user_type == user_constants.SUPER_ADMIN:
            return models.Project.objects.all()
        elif self.request.user.user_type == user_constants.ADMIN:
            return models.Project.objects.filter(organisation=self.request.user)
        elif self.request.user.user_type == user_constants.PROJECT_MANAGER:
            return models.ProjectUser.objects \
                .select_related('project') \
                .filter(user=self.request.user)


class Assign(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ProjectUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return ProjectUser.objects.create()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
