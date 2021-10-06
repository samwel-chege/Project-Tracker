from django.conf.urls import url, include
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/', views.profile, name='profile'),
    path('cohort/<name>/', views.cohort, name='cohort'),
    path('project/<title>/', views.project, name='project'),
]