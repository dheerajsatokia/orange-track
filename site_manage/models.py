from django.db import models
from project_management.models import Project


class Site(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='Project')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
