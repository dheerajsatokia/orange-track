from django.db import models

from user.models import Organisation, User


class ProjectUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('project_management.Project', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.nick_name


class Project(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=5)
    is_government = models.BooleanField()
    users = models.ManyToManyField(to=User, through=ProjectUser)

    def __str__(self):
        return self.title

