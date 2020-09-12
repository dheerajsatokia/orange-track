from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from project_management.views import Assign
from . import views

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'', views.ProjectViewSet, basename='project')
# router.register(r'assign', views.A, basename='project')

urlpatterns = [
    path('assign', Assign.as_view({
        'get': 'list',
        'post': 'create'
    }))
]
urlpatterns += format_suffix_patterns(router.urls)
