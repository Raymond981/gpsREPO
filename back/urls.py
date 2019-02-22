
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from rest_framework.authtoken import views
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()


urlpatterns = [
    re_path(r'^api/v1/login',include('Login.urls')),
    re_path('api/v1/gps/',include('gps.urls')),
    re_path('api/v1/register/',include('Register.urls')),
    re_path('api/v1/unidades/',include('Unidades.urls')),
    re_path('api/v1/profile/',include('Profile.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls))
]