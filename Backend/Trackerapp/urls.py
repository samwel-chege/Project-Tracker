from django.urls import include, path
from .views import RegisterView, VerifyEmail
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import views

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify')


]