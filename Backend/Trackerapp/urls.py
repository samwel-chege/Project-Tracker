from os import name
from django.urls import include, path
from .views import (
     RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, 
     RequestPasswordResetEmail, SetNewPasswordAPIView, LogoutAPIView)
from rest_framework import views
from rest_framework_simplejwt.views import TokenRefreshView

from django.conf.urls import url, include
from .views import *

from .views import RegisterView, VerifyEmail, LoginAPIView

from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import Http404

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),


    # path('signup/', views.signup, name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')


    # All Students
    url(r'api/students/all/$', StudentList.as_view(), name='api_students'),

    # Create new Student
    url(r'^api/students/new/$', NewStudentView.as_view(), name='api_new_student'),

    # Student search
    url(r'api/search/students/$', StudentSearch.as_view(), name='api_student_search'),

    # Student Profile by id
    url(r'api/students/(?P<pk>[0-9]+)/$', StudentProfileView.as_view(), name='api_student'),



    # All Projects
    url(r'api/projects/all/$', ProjectList.as_view(), name='api_projects'),

    # Create new Project
    url(r'^api/projects/new/$', NewProjectView.as_view(), name='api_new_project'),

    # Project search
    url(r'api/search/projects/$', ProjectSearch.as_view(), name='api_project_search'),

    # Project profile by id
    url(r'api/projects/(?P<pk>[0-9]+)/$', ProjectProfileView.as_view(), name='api_project'),



    # All Languages/Development Styles
    url(r'^api/styles/all/$', StylesView.as_view(), name='api_styles'),

    # DevStyle profile by id
    url(r'api/styles/(?P<pk>[0-9]+)/$', StyleProfileView.as_view(), name='api_style'),

    # All Projects filtered by DevStyle
    url(r'api/styles/(?P<pk>[0-9]+)/projects/$', ProjectsByDevStyleView.as_view(), name='api_projects_style'),



    # All Cohorts/Classes
    url(r'^api/cohorts/all/$', CohortsView.as_view(), name='api_cohorts'),

    # Cohort Profile by id
    url(r'api/cohorts/(?P<pk>[0-9]+)/$', CohortProfileView.as_view(), name='api_cohort'),

    # Create new Cohort
    url(r'^api/cohorts/new/$', NewCohortView.as_view(), name='api_new_cohort'),

    # All Cohort Members
    url(r'api/cohorts/(?P<pk>[0-9]+)/members/$', CohortMembersView.as_view(), name='api_cohort_members'),

    # All Projects filtered by Cohort
    url(r'api/cohorts/(?P<pk>[0-9]+)/projects/$', ProjectsByCohortView.as_view(), name='api_projects_cohort'),

# authentication url paths
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirmation' ),
    path('password-reset-success/', SetNewPasswordAPIView.as_view(), name='password-reset-success'),



]