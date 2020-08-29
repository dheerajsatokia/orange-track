from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseMode(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    username = None  # Disregard built-in username field
    nick_name = models.CharField(max_length=255, blank=True, null=True)
    password_hint = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    apt_suite = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    union = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    social_media = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    user_type = models.CharField(max_length=2)

    # Customized User settings
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Organisation(models.Model):
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Site(models.Model):
    project = models.ForeignKey(Organisation, on_delete=models.CASCADE)


# Inventory
class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sku = models.CharField(max_length=5)
    price = models.IntegerField()


class Vendor(models.Model):
    name = models.CharField()


class PurchaseRecord(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    purchase_type = models.CharField()
    vendor = models.CharField(max_length=255)
    quantity = models.IntegerField()


# Stages
class Stage(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class Block(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    title = models.CharField(max_length=5)


class Level(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)


# Tasks
class Tasks(models.Model):
    task_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2)
    deadline = models.DateTimeField(null=True)


class TaskRemarks(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)


# Meeting
class Meeting(models.Model):
    title = models.CharField(max_length=255)
    starting_datetime = models.DateTimeField()
    end_time = models.TimeField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField()
    attachment = models.FileField(null=True, blank=True)


class Agenda(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    description = models.ForeignKey(Meeting, on_delete=models.CASCADE)


class MeetingAttendees(models.Model):
    # Automatically add creater to attandees
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=3)


class MOM(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()


# Drawings
class Plans(models.Model):
    title = models.CharField(max_length=255)


class PlanOption(models.Model):
    title = models.CharField(max_length=255)


class Drawing(models.Model):
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    parent_option = models.ForeignKey(PlanOption, on_delete=models.CASCADE)
    details = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DrawingRemark(models.Model):
    remarked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
    crated_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField()


# Issue
class Issue(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    description = models.TextField()
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    assigned_to = models.CharField(max_length=10)
    status = models.CharField(max_length=5)


class IssueImage(models.ForeignKey):
    image = models.ForeignKey(Issue, on_delete=models.CASCADE)


class IssueRemark(models.Model):
    remark = models.TextField()


class Notification(models.Model):
    notification_message = models.TextField()


class ProgressEntries(models.Model):
    pass


# Staff
class StaffCategory(models.Model):
    type = models.CharField(max_length=8)


class StaffSubType(models.Model):
    type = models.CharField(max_length=8)
    staff_category = models.ForeignKey(StaffCategory, on_delete=models.CASCADE)


class StaffAttendance(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    staff_type = models.ForeignKey(StaffSubType, on_delete=models.CASCADE)
    staff_count = models.PositiveIntegerField()
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class VendorVisit(models.Model):
    vendor = models.ForeignKey(Vendor)
    work_done = models.TextField()
    time_taken = models.IntegerField()  # In minutes
