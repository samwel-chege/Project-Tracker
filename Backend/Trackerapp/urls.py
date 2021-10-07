from django.conf.urls import url, include
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls')),
    # path('profile/<id>/', views.profile, name='profile'),
    # path('cohort/<name>/', views.cohort, name='cohort'),
    # path('project/<title>/', views.project, name='project'),
    # path('language/<name>/', views.language, name='language'),
    # path('profiles/', views.all_profiles, name='all_profiles'),
    # path('projects/', views.all_projects, name='all_projects'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)