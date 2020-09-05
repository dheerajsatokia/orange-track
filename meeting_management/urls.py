from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'^create', views.MeetingViewSet, basename='create-meeting')
router.register(r'^agenda', views.AgendaViewSet, basename='agenda')
router.register(r'^minutes', views.MOMViewSet, basename='minutes')
router.register(r'^attendees', views.MeetingAttendeesViewSet, basename='attendees')

urlpatterns = [
]
urlpatterns += format_suffix_patterns(router.urls)
