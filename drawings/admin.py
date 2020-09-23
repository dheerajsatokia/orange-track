from django.contrib import admin
from .models import Plans, PlanOption, Drawing, DrawingRemark

# Register your models here.
admin.site.register(Plans)
admin.site.register(PlanOption)
admin.site.register(Drawing)
admin.site.register(DrawingRemark)
