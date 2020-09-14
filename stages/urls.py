from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'sub-stage', views.SubStageViewSet)
router.register(r'block', views.BlockViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'progress-entry', views.ProgressEntryViewSet)
router.register(r'progress-inventory-entry', views.ProgressInventoryEntryViewSet)
router.register(r'', views.StageViewSet)

urlpatterns = [
    # path('approve-entry', views.ApproveEntry())
]
urlpatterns += format_suffix_patterns(router.urls)
