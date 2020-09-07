from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'sub-stage', views.SubStageViewSet)
router.register(r'block', views.BlockViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'', views.StageViewSet)

urlpatterns = [
]
urlpatterns += format_suffix_patterns(router.urls)
