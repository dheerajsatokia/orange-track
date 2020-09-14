from django.db import models

from project_management.models import Project
from user.models import User


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


class VendorVisit(models.Model):
    vendor = models.ForeignKey('inventory.Vendor', on_delete=models.CASCADE)
    work_done = models.TextField()
    time_taken = models.IntegerField()  # In minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
