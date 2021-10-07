from django.urls import include, path
from django.conf.urls import url, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url('^$', views.home, name='home'),
    path('register', RegisterView.as_view(), name='register'),
    url(r'^api/students/$', StudentView.as_view(), name='api_students'),
    url(r'^api/projects/$', ProjectView.as_view(), name='api_projects'),
    url(r'^api/styles/$', StyleView.as_view(), name='api_styles'),
    url(r'^api/cohorts/$', CohortView.as_view(), name='api_cohorts'),

    # path('signup/', views.signup, name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
]