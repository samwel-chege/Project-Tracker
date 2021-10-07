from django.urls import include, path
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import views

urlpatterns = [
    path('register', RegisterView.as_view(), name='register')

    # path('signup/', views.signup, name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
]