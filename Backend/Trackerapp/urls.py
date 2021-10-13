from django.urls import include, path

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
    path('login/', LoginAPIView.as_view(), name='login'),
    path('accountverify/', VerifyEmail.as_view(), name='accountverify'),


    ## Cleaner urls

    url(r'^api/users/$', CustomUsersList.as_view(), name='api_customusers'),    # All CustomUsers
    url(r'^api/users/(?P<pk>[0-9]+)/$', CustomUserView.as_view(), name='api_customuser_profile'),    # CustomUserProfile
    url(r'^api/users/(?P<pk>[0-9]+)/update/$', UpdateCustomUserView.as_view(), name='api_update_customuser'),    # Update CustomUser

    url(r'^api/cohorts/$', CohortsList.as_view(), name='api_cohorts'),    # Get all Cohorts + Create
    url(r'api/cohorts/(?P<pk>[0-9]+)/$', CohortProfileView.as_view(), name='api_cohort'),    # Cohort by id + Delete

    url(r'^api/styles/$', StylesList.as_view(), name='api_styles'),    # Get all Styles + Create
    url(r'api/styles/(?P<pk>[0-9]+)/$', StyleProfileView.as_view(), name='api_style'),    # DevStyle by id + Delete

    url(r'^api/projects/$', ProjectsList.as_view(), name='api_projects'),    # Get all Projects
    url(r'^api/projects/new/$', NewProjectView.as_view(), name='api_new_project'),    # Create new project
    url(r'api/projects/(?P<pk>[0-9]+)/$', ProjectProfileView.as_view(), name='api_project'),    # Project by id + Delete + ProjectMembers
    url(r'api/projects/(?P<pk>[0-9]+)/update/$', UpdateProjectView.as_view(), name='api_update_project'),    # Update Project
    url(r'api/projects/(?P<pk>[0-9]+)/update/members/$', UpdateProjectMembersView.as_view(), name='api_update_projectmembers'),    # Update Project Members

    url(r'^api/students/$', StudentsList.as_view(), name='api_students'),    # Get all Students
    url(r'api/students/(?P<pk>[0-9]+)/$', StudentProfileView.as_view(), name='api_student'),    # Student by id + StudentProjects
    url(r'api/students/(?P<pk>[0-9]+)/update/$', UpdateStudentView.as_view(), name='api_update_student'),    # Update Student profile

    url(r'api/search/projects/$', ProjectSearch.as_view(), name='api_project_search'),    # Project search
    url(r'api/search/students/$', StudentSearch.as_view(), name='api_student_search'),    # Student search

]