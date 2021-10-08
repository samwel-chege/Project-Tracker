from django.urls import include, path
from django.conf.urls import url, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    url(r'^api/students/$', StudentView.as_view(), name='api_students'),
    url(r'^api/projects/$', ProjectView.as_view(), name='api_projects'),
    url(r'^api/styles/$', StyleView.as_view(), name='api_styles'),
    url(r'^api/cohorts/$', CohortView.as_view(), name='api_cohorts'),
    url(r'api/styles/(?P<pk>[0-9]+)/$', ProjectDevModeView.as_view(), name='api_style'),
    url(r'api/students/(?P<pk>[0-9]+)/$', StudentProfile.as_view(), name='api_student'),
    url(r'api/cohorts/(?P<pk>[0-9]+)/$', CohortMembersView.as_view(), name='api_cohort')

    # path('signup/', views.signup, name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
]