from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from OrangeTrackBackend import user_permissions
from OrangeTrackBackend.constants import user_constants, read_actions
from project_management.serializer import ProjectUserSerializer, ProjectSerializer
from . import models


def get_project_queryset(request, user):
    if user.user_type == user_constants.SUPER_ADMIN:
        return models.Project.objects.all()
    elif user.user_type == user_constants.ADMIN:
        return models.Project.objects.filter(organisation=request.organisation)
    elif user.user_type in [user_constants.PROJECT_MANAGER, user_constants.SITE_ENGINEER]:
        return models.ProjectUser.objects \
            .select_related('project') \
            .filter(user=user)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissionsfsdf(self):
        if self.action in read_actions:
            permission_classes = [user_permissions.AboveProjectManager, ]
        else:
            permission_classes = [user_permissions.AboveAdmin, ]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return get_project_queryset(self.request, self.request.user)


class Assign(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, user_permissions.AboveProjectManager)
    serializer_class = ProjectUserSerializer

    def get_queryset(self):
        return get_project_queryset(self.request, self.request.user)
