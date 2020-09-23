from django.contrib import admin

# Register your models here.
from .models import Stage, SubStage, Block, Level, ProgressEntry, ProgressInventoryEntry, ProgressEntryMedia, \
    ProgressComment


class StageAdmin(admin.ModelAdmin):
    search_fields = ['project', 'title']
    list_display = ('title', 'created_at', 'updated_at', 'project')
    fields = ('title', 'project')


class SubStageAdmin(admin.ModelAdmin):
    search_fields = ['project']
    list_display = ('title', 'stage', 'created_at', 'updated_at')
    fields = ('stage', 'title', 'inventory')
    # list_filter = ('user',)


class BlockAdmin(admin.ModelAdmin):
    search_fields = ['project']
    list_display = ('title', 'created_at', 'updated_at', 'sub_stage')
    fields = ('title', 'sub_stage')


class LevelAdmin(admin.ModelAdmin):
    search_fields = ['project']
    list_display = ('title', 'created_at', 'updated_at', 'block')
    fields = ('title', 'block')


class ProgressEntryAdmin(admin.ModelAdmin):
    search_fields = ['block']
    list_display = ('block', 'is_approved')
    fields = ('block', 'is_approved')
    list_filter = ('is_approved',)


class ProgressInventoryEntryAdmin(admin.ModelAdmin):
    search_fields = ['progress_entry', 'inventory']
    list_display = ('progress_entry', 'inventory', 'quantity', 'last_updated', 'created_at', 'created_by')
    fields = ('progress_entry', 'inventory', 'quantity')
    readonly_fields = ('created_by',)

    # list_filter = ('is_approved',)


class ProgressEntryMediaAdmin(admin.ModelAdmin):
    search_fields = ['progress_entry']
    list_display = ('media', 'progress_entry')
    fields = ('media', 'progress_entry')
    # list_filter = ('is_approved',)


class ProgressCommentAdmin(admin.ModelAdmin):
    search_fields = ['progress_entry', 'inventory']
    list_display = ('progress_entry', 'comment', 'last_updated', 'created_at', 'created_by')
    readonly_fields = ('created_by',)
    fields = ('progress_entry', 'comment')


admin.site.register(Stage, StageAdmin)
admin.site.register(SubStage, SubStageAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(ProgressEntry, ProgressEntryAdmin)
admin.site.register(ProgressInventoryEntry, ProgressInventoryEntryAdmin)
admin.site.register(ProgressEntryMedia, ProgressEntryMediaAdmin)
admin.site.register(ProgressComment, ProgressCommentAdmin)
