from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'staff-category', views.StaffCategoryViewSet)
router.register(r'staff-subtype', views.StaffSubTypeViewSet)
router.register(r'staff-attendance', views.StaffAttendanceViewSet)

urlpatterns = [
]
urlpatterns += format_suffix_patterns(router.urls)
