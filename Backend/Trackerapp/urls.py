from django.urls import include, path
from django.conf.urls import url, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),

    url(r'^api/students/$', StudentsView.as_view(), name='api_students'),
    url(r'^api/students/new/$', NewStudentView.as_view(), name='api_new_student'),
    url(r'api/students/(?P<pk>[0-9]+)/$', StudentProfileView.as_view(), name='api_student'),

    url(r'^api/projects/$', ProjectsView.as_view(), name='api_projects'),
    url(r'^api/projects/new/$', NewProjectView.as_view(), name='api_new_project'),
    url(r'api/projects/(?P<pk>[0-9]+)/$', ProjectProfileView.as_view(), name='api_project'),

    url(r'^api/styles/$', StylesView.as_view(), name='api_styles'),
    url(r'api/styles/(?P<pk>[0-9]+)/$', StyleProfileView.as_view(), name='api_style'),
    url(r'api/styles/(?P<pk>[0-9]+)/projects$', ProjectsByDevStyleView.as_view(), name='api_projects_style'),

    url(r'^api/cohorts/$', CohortsView.as_view(), name='api_cohorts'),
    url(r'api/cohorts/(?P<pk>[0-9]+)/$', CohortProfileView.as_view(), name='api_cohort'),
    url(r'api/cohorts/(?P<pk>[0-9]+)/members/$', CohortMembersView.as_view(), name='api_cohort_members'),
    url(r'api/cohorts/(?P<pk>[0-9]+)/projects/$', ProjectsByCohortView.as_view(), name='api_projects_cohort'),

    # path('signup/', views.signup, name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
]