from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from site_manage.views import Assign
from django.urls import path

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'site', views.SiteViewSet)

urlpatterns = [
    path('assign', Assign.as_view())
]
urlpatterns += format_suffix_patterns(router.urls)
