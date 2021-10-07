from django.conf.urls import url, include
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls')),
    path('student/<id>/', views.student, name='student'),
    path('cohort/<name>/', views.cohort, name='cohort'),
    path('project/<title>/', views.project, name='project'),
    path('language/<name>/', views.language, name='language'),
    path('students/', views.all_students, name='all_students'),
    path('projects/', views.all_projects, name='all_projects'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)