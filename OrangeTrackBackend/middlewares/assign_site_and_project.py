import logging

from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication

from project_management.models import ProjectUser
from site_manage.models import SiteUser
from user.models import UserOrganisation

# request_logger = logging.getLogger('django.request')
request_logger = logging.getLogger(__name__)


class AssignSiteAndProject(MiddlewareMixin):
    """Request Logging Middleware."""

    def process_request(self, request, *args, **kwargs):
        user = self.__get_user_jwt(request)
        if not user or user.is_anonymous:
            request.project = None
            request.organisation = None
            request.site = None
            return None

        request.project = self._get_project(user)
        request.organisation = self.__get_organisation(user)
        request.site = self.__get_site(user)

    def _get_project(self, user):
        return getattr(ProjectUser.objects.filter(user=user).first(), 'project', None)

    def __get_organisation(self, user):
        return getattr(UserOrganisation.objects.filter(user=user).first(), 'organization', None)

    def __get_site(self, user):
        return getattr(SiteUser.objects.filter(user=user).first(), 'site', None)

    def __get_user_jwt(self, request):
        """
        Replacement for django session auth get_user & auth.get_user
         JSON Web Token authentication. Inspects the token for the user_id,
         attempts to get that user from the DB & assigns the user on the
         request object. Otherwise it defaults to AnonymousUser.

        This will work with existing decorators like LoginRequired  ;)

        Returns: instance of user object or AnonymousUser object
        """
        user = None
        try:
            user_jwt = JWTAuthentication().authenticate(Request(request))
            if user_jwt is not None:
                # store the first part from the tuple (user, obj)
                user = user_jwt[0]
        except:
            pass

        return user or AnonymousUser()
