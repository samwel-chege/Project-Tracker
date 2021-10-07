from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
import django.contrib.auth.views

urlpatterns = [
    path('admin/', admin.site.urls),
]
