from django.db.models.fields import IPAddressField
from django.shortcuts import render
from rest_framework import generics, serializers,status
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

# Create your views here.
class RegisterView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer =self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data =serializer.data
        user = CustomUser.objects.get(email=user_data('email'))
        token = RefreshToken.for_user(user).access_token

        current_site=get_current_site(request)
        relativeLink=reverse('email-verify')
        absoluteurl='http://'+current_site+relativeLink+"?token="+token
        email_body='Click on the link below to verify your email'
        data={'email_body':email_body, 'email_subject':'Verify your email \n'+ absoluteurl}

        Util.dend_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass