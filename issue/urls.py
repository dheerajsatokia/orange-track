from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'^image', views.IssueImageViewSet, basename='image')
router.register(r'^remark', views.IssueRemarkViewSet, basename='remark')
router.register(r'^notification', views.NotificationViewSet, basename='notification')
router.register(r'^', views.IssueViewSet, basename='create')


urlpatterns = [
]
urlpatterns += format_suffix_patterns(router.urls)
