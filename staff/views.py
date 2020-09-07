from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializer
from . import models


class StaffCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.StaffCategory.objects.all()
    serializer_class = serializer.StaffCategorySerializer


class StaffSubTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.StaffSubType.objects.all()
    serializer_class = serializer.StaffSubTypeSerializer


class StaffAttendanceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.StaffAttendance.objects.all()
    serializer_class = serializer.StaffAttendanceSerializer
