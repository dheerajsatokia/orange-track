from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from project_management import serializer as project_serializer
from project_management.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = project_serializer.ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()
