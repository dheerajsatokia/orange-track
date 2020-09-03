# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from . import serializers
from . import models


# Create your views here.


class StageViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Stage.objects.all()
    serializer_class = serializers.StageSerializer


class SubStageViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    queryset = models.SubStage.objects.all()
    serializer_class = serializers.SubStageSerializer


class BlockViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Block.objects.all()
    serializer_class = serializers.BlockSerializer
