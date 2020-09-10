from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializer
from . import models


class SiteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Site.objects.all()
    serializer_class = serializer.SiteSerializer

    def get_queryset(self):
        # if project_manager:
        #     return models.Site.objects.filter(project=self.request.project)
        # if site_manager:

            return models.SiteUser.objects \
                .select_related('site') \
                .filter(user=self.request.user)
