from django.urls import include, path
from .views import RegisterView, VerifyEmail, LoginAPIView
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import views

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify')


]