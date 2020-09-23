from django.contrib import admin

from .models import Project, ProjectUser


class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['title', 'organisation']
    list_display = ('title', 'description', 'state', 'is_government', 'created_at', 'updated_at', 'organisation')
    fields = ('title', 'description', 'state', 'is_government', 'created_at', 'updated_at', 'organisation')
    # list_filter = ('user',)


class ProjectUserAdmin(admin.ModelAdmin):
    search_fields = ['project']
    list_display = ('project', 'user', 'is_admin')
    fields = ('project', 'user', 'is_admin')
    list_filter = ('user',)


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectUser, ProjectUserAdmin)
