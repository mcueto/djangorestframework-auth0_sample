"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import (
    url,
    include,
)
from django.contrib import admin
from rest_framework import routers
from .views import (
    AllToDosViewSet,
    SecureToDosViewSet,
    AdminToDosViewSet,
    MyOwnToDosViewSet,
    ToDoViewSet,
)

router = routers.DefaultRouter()
# All users
router.register(
    'all-todos',
    AllToDosViewSet
)
# Only authenticated users
router.register(
    'secure-todos',
    SecureToDosViewSet
)
# Authenticated users with group validation(similar to role o permission validation)
router.register(
    'admin-todos',
    AdminToDosViewSet
)
# Authenticated user that can only see it's ToDos and when create a ToDo it's
# automatically associated to it
router.register(
    'my-todos',
    MyOwnToDosViewSet,
    basename='myowntodos'
)
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
