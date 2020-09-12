from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'^', views.UserViewSet, basename='user')
router.register(r'^organisation', views.OrganisationViewSet, basename='organisation')

urlpatterns = [
    path('assign', views.Assign.as_view({
        'get': 'list',
        'post': 'create'
    }))
]
urlpatterns += format_suffix_patterns(router.urls)
