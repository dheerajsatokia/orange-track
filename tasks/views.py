from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework.permissions import IsAuthenticated


class TasksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Tasks.objects.all()
    serializer_class = serializer.TasksSerializer


class TaskRemarksViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.TaskRemarks.objects.all()
    serializer_class = serializer.TaskRemarksSerializer
