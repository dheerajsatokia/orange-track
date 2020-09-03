from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

routers = routers.SimpleRouter(trailing_slash=False)
routers.register(r'tasks', views.TasksViewSet)
routers.register(r'tasks-remarks', views.TaskRemarksViewSets)

urlpatterns = [
]
urlpatterns += format_suffix_patterns(routers.urls)
