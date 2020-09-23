from django.contrib import admin
from .models import User, Organisation, UserOrganisation

# Register your models here.
admin.site.site_header = 'Orange Track'


class UserOrganisationAdmin(admin.ModelAdmin):
    list_display = ('organization', 'user', 'is_admin')


admin.site.register(User)
admin.site.register(Organisation)
admin.site.register(UserOrganisation, UserOrganisationAdmin)
