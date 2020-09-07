from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializer
from . import models


class SiteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Site.objects.all()
    serializer_class = serializer.SiteSerializer
