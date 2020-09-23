from django.db import models

from user.models import User
from project_management.models import Project
from stages.models import Stage


# Issue
class Issue(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    description = models.TextField()
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=10)
    status = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.stage.title


class IssueImage(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    image = models.FileField(upload_to='image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image


class IssueRemark(models.Model):
    remark = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.remark


class Notification(models.Model):
    notification_message = models.TextField()

    def __str__(self):
        return self.notification_message


class ProgressEntries(models.Model):
    pass
