from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from OrangeTrackBackend import user_permissions
from . import models
from . import serializers


class StageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, user_permissions.AboveSiteEngineer)
    queryset = models.Stage.objects.all()
    serializer_class = serializers.StageSerializer


class SubStageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, user_permissions.AboveSiteEngineer)
    queryset = models.SubStage.objects.all()
    serializer_class = serializers.SubStageSerializer


class BlockViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, user_permissions.AboveSiteEngineer)
    queryset = models.Block.objects.all()
    serializer_class = serializers.BlockSerializer


class LevelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, user_permissions.AboveSiteEngineer)
    queryset = models.Level.objects.all()
    serializer_class = serializers.LevelSerializer


class ProgressInventoryEntryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, user_permissions.AboveSiteEngineer)
    queryset = models.ProgressInventoryEntry.objects.all()
    serializer_class = serializers.ProgressInventoryEntrySerializer


class ProgressEntryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, user_permissions.AboveProjectManager)
    queryset = models.ProgressEntry.objects.all()
    serializer_class = serializers.ProgressEntrySerializer
