"""OrangeTrackBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
    path('auth/', include('user.auth_urls')),
    path('user/', include('user.urls')),
    path('project/', include('project_management.urls')),
    path('inventory/', include('inventory.urls')),
    path('meeting/', include('meeting_management.urls')),
    path('issue/', include('issue.urls')),
    path('staff/', include('staff.urls')),
    path('drawings/', include('drawings.urls')),
    path('site_manage/', include('site_manage.urls')),
    path('stage/', include('stages.urls')),
    path('tasks/', include('tasks.urls'))
]
