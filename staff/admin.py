from django.contrib import admin
from staff.models import StaffCategory, StaffSubType, StaffAttendance

# Register your models here.

admin.site.register(StaffCategory)
admin.site.register(StaffSubType)
admin.site.register(StaffAttendance)
