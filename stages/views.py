from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models


class StageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Stage.objects.all()
    serializer_class = serializers.StageSerializer


class SubStageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.SubStage.objects.all()
    serializer_class = serializers.SubStageSerializer


class BlockViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Block.objects.all()
    serializer_class = serializers.BlockSerializer


class LevelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Level.objects.all()
    serializer_class = serializers.LevelSerializer
