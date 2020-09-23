from django.contrib import admin
from site_manage.models import Site, SiteUser

# Register your models here.

admin.site.register(Site)
admin.site.register(SiteUser)