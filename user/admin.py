from django.contrib import admin
from .models import User, Organisation, UserOrganisation

# Register your models here.
admin.site.site_header = 'Orange Track'


class UserOrganisationAdmin(admin.ModelAdmin):
    search_fields = ['organization']
    list_display = ('organization', 'user', 'is_admin')
    fields = ('organization', 'user', 'is_admin')
    list_filter = ('user',)


class OrganisationAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'brand', 'email', 'phone', 'website')
    fields = ('title', 'brand', 'email', 'phone', 'website')


class UserAdmin(admin.ModelAdmin):
    search_fields = ['nick_name', 'email']
    list_display = ('nick_name', 'email', 'phone', 'user_type')
    fields = ('nick_name', 'email', 'street', 'city', 'state', 'zip_code', 'phone', 'user_type')
    list_filter = ('user_type',)


admin.site.register(User, UserAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(UserOrganisation, UserOrganisationAdmin)
