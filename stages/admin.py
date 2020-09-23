from django.contrib import admin

# Register your models here.
from .models import Stage, SubStage, Block, Level, ProgressEntry



admin.site.register(Stage)
admin.site.register(SubStage)
admin.site.register(Block)
admin.site.register(Level)
admin.site.register(ProgressEntry)
