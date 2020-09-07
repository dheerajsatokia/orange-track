from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializer
from . import models


class PlansViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Plans.objects.all()
    serializer_class = serializer.PlansSerializer


class PlanOptionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.PlanOption.objects.all()
    serializer_class = serializer.PlanOptionSerializer


class DrawingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Drawing.objects.all()
    serializer_class = serializer.DrawingSerializer


class DrawingRemarkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.DrawingRemark.objects.all()
    serializer_class = serializer.DrawingRemarkSerializer
