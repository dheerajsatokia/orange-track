from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'plans', views.PlansViewSet)
router.register(r'plan-option', views.PlanOptionViewSet)
router.register(r'drawing', views.DrawingViewSet)
router.register(r'drawing-remark', views.DrawingRemarkViewSet)

urlpatterns = [
]
urlpatterns += format_suffix_patterns(router.urls)
