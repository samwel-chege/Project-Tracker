from django.urls import include, path
from django.conf.urls import url
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import views

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    url(r'^api/profiles/$', StudentView.as_view(), name='api_students'),
    url(r'^api/projects/$', ProjectView.as_view(), name='api_projects'),
    url(r'^api/styles/$', StyleView.as_view(), name='api_styles'),
    url(r'^api/cohorts/$', CohortView.as_view(), name='api_cohorts'),

    # path('signup/', views.signup, name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
]