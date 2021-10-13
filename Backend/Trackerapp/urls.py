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


    url(r'api/students/all/$', StudentList.as_view(), name='api_students'),    # All Students
    url(r'^api/students/(?P<pk>[0-9]+)/update/$', UpdateStudentProfileView.as_view(), name='api_update_student'),    # Update Student Profile
    url(r'api/students/(?P<pk>[0-9]+)/$', StudentProfileView.as_view(), name='api_student'),    # Student Profile by id


    url(r'api/projects/all/$', ProjectList.as_view(), name='api_projects'),    # All Projects
    url(r'^api/projects/new/$', NewProjectView.as_view(), name='api_new_project'),    # Create new Project
    url(r'api/projects/(?P<pk>[0-9]+)/$', ProjectProfileView.as_view(), name='api_project'),    # Project profile by id
    url(r'^api/projects/(?P<pk>[0-9]+)/update/$', UpdateProjectView.as_view(), name='api_update_project'),    # Update Project
    url(r'^api/projects/(?P<pk>[0-9]+)/update/members/$', UpdateProjectMembersView.as_view(), name='api_update_members'),    # Update Project Members


    url(r'^api/styles/all/$', StylesView.as_view(), name='api_styles'),    # All Languages/Development Styles
    url(r'^api/styles/new/$', NewStyleView.as_view(), name='api_new_style'),    # Create new Style
    url(r'api/styles/(?P<pk>[0-9]+)/$', StyleProfileView.as_view(), name='api_style'),    # DevStyle profile by id
    url(r'api/styles/(?P<pk>[0-9]+)/projects/$', ProjectsByDevStyleView.as_view(), name='api_projects_style'),    # All Projects filtered by DevStyle


    url(r'^api/cohorts/all/$', CohortsView.as_view(), name='api_cohorts'),    # All Cohorts/Classes
    url(r'^api/cohorts/new/$', NewCohortView.as_view(), name='api_new_cohort'),    # Create new Cohort
    url(r'api/cohorts/(?P<pk>[0-9]+)/$', CohortProfileView.as_view(), name='api_cohort'),    # Cohort Profile by id
    url(r'api/cohorts/(?P<pk>[0-9]+)/members/$', CohortMembersView.as_view(), name='api_cohort_members'),    # All Cohort Members
    url(r'api/cohorts/(?P<pk>[0-9]+)/projects/$', ProjectsByCohortView.as_view(), name='api_projects_cohort'),    # All Projects filtered by Cohort


    url(r'api/search/projects/$', ProjectSearch.as_view(), name='api_project_search'),    # Project search
    url(r'api/search/students/$', StudentSearch.as_view(), name='api_student_search'),    # Student Profile by id


    url(r'^api/users/(?P<pk>[0-9]+)/update/$', UpdateCustomUserView.as_view(), name='api_update_user'),    # Update CustomUser
]