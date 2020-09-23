from django.contrib import admin
from .models import User, Organisation, UserOrganisation

# Register your models here.
admin.site.site_header = 'Orange Track'
admin.site.register(User)
admin.site.register(Organisation)
admin.site.register(UserOrganisation)

