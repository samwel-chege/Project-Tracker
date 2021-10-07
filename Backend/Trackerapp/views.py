from django.db.models.fields import IPAddressField
from django.shortcuts import render
from rest_framework import generics, serializers,status

from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token

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
        token = RefreshToken.for_user(user)
        return Response(user_data, status=status.HTTP_201_CREATED)