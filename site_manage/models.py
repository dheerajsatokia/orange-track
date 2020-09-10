from django.db import models

from project_management.models import Project


class SiteUser(models.Model):
    site = models.ForeignKey('site_manage.Site', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)


class Site(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='Project')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
