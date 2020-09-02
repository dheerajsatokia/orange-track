from django.db import models

from user.models import User
from project_management.models import Project


# Staff
class StaffCategory(models.Model):
    type = models.CharField(max_length=8)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class StaffSubType(models.Model):
    type = models.CharField(max_length=8)
    staff_category = models.ForeignKey(StaffCategory, on_delete=models.CASCADE)


class StaffAttendance(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    staff_type = models.ForeignKey(StaffSubType, on_delete=models.CASCADE)
    staff_count = models.PositiveIntegerField()
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
