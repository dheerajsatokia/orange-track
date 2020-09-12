from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from site_manage.serializer import SiteSerializer, SiteUserSerializer
from . import models
from OrangeTrackBackend.constants import user_constants
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SiteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Site.objects.all()
    serializer_class = SiteSerializer

    def get_queryset(self):
        if self.request.user.user_type == user_constants.SUPER_ADMIN:
            return models.Site.objects.all()
        elif self.request.user.user_type == user_constants.ADMIN:
            return models.Site.objects.filter(project__organisation=self.request.organisation)
        elif self.request.user.user_type == user_constants.PROJECT_MANAGER:
            return models.Site.objects.filter(project=self.request.project)
        elif self.request.user.user_type == user_constants.SITE_ENGINEER:
            return models.SiteUser.objects \
                .select_related('site') \
                .filter(user=self.request.user)


    # def get_queryset(self):
    # if project_manager:
    #     return models.Site.objects.filter(project=self.request.project)
    # if site_manager:

    # return models.SiteUser.objects \
    #     .select_related('site') \
    #     .filter(user=self.request.user)

class Assign(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = SiteUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return models.SiteUser.objects.create()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



