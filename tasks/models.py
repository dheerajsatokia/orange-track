from django.db import models

from user.models import User
from project_management.models import Project


# Tasks
class Tasks(models.Model):
    task_description = models.TextField()
    assigned_to = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='assigned_to')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    status = models.CharField(max_length=2)
    deadline = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class TaskRemarks(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)