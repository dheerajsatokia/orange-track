from django.contrib import admin
from .models import User

# Register your models here.
admin.site.site_header = 'Orange Track'
admin.site.register(User)
