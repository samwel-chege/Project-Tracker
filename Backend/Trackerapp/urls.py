from os import name
from django.urls import include, path
from .views import (
     RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, 
     RequestPasswordResetEmail, SetNewPasswordAPIView, LogoutAPIView)
from rest_framework import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirmation' ),
    path('password-reset-success/', SetNewPasswordAPIView.as_view(), name='password-reset-success'),


]