from rest_framework.permissions import BasePermission

from OrangeTrackBackend.constants import user_constants

_above_admin = [user_constants.SUPER_ADMIN, user_constants.ADMIN]
_above_project_manager = [user_constants.PROJECT_MANAGER] + _above_admin
_above_site_engineer = [user_constants.SITE_ENGINEER] + _above_project_manager


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_super_admin)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_admin)


class IsProjectManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_project_manager)


class IsSiteEngineer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_site_engineer)


class AboveSiteEngineer(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in _above_site_engineer


class AboveAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in _above_admin


class AboveProjectManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in _above_project_manager
