from django.contrib.auth.models import AbstractUser
from django.db import models

from OrangeTrackBackend.constants import user_constants


# Create your models here.
class User(AbstractUser):
    username = None  # Disregard built-in username field
    nick_name = models.CharField(max_length=255, blank=True, null=True)
    password_hint = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    Type_Choices = (
        (user_constants.SUPER_ADMIN, 'Super Admin'),
        (user_constants.ADMIN, 'Admin'),
        (user_constants.ARCHITECTURE, 'Architecture'),
        (user_constants.PROJECT_MANAGER, 'Project Manager'),
        (user_constants.SITE_ENGINEER, 'Site Engineer'),
        (user_constants.SUB_CONTRACTOR, 'Sub Contractor'),
        (user_constants.DEFAULT_USER, 'Sub Contractor')

    )
    user_type = models.IntegerField(choices=Type_Choices, default=user_constants.SUB_CONTRACTOR)

    # Customized User settings
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class UserOrganisation(models.Model):
    organization = models.ForeignKey('user.Organisation', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)


class Organisation(models.Model):
    title = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, through=UserOrganisation)

    def __str__(self):
        return self.title
