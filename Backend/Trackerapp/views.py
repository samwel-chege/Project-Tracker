from django.db.models.fields import IPAddressField
from django.shortcuts import render
from rest_framework import generics, serializers,status,views
from .models import CustomUser
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, ResetPasswordEmailRequestSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UserRender
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
 


# Create your views here.
class RegisterView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    renderer_classes = (UserRender,)

    def post(self, request):
        user = request.data
        serializer =self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data =serializer.data
        user = CustomUser.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site=get_current_site(request).domain
        relativeLink=reverse('email-verify')
        absoluteurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body='Click on the link below to verify your email  \n'+ absoluteurl
        data={'email_body':email_body,'to_email':user.email, 'email_subject':'Verify your email'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token=request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY,algorithms=['HS256'])
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Ivalid token, request a new one'}, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer =  self.serializer_class(data=request.data)
        email = request.data.get('email', '')
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64=urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site=get_current_site(request=request).domain
            relativeLink=reverse(
                'password-reset-confirmation', kwargs={'uidb64': uidb64, 'token': token})
            absoluteurl = 'http://'+current_site+relativeLink
            email_body='Hello, \n Click on the link below to reset your password  \n'+ absoluteurl
            data={'email_body':email_body,'to_email':user.email, 'email_subject':'Reset your password'}

            Util.send_email(data)
        return Response({'Successful reset: ' 'A link has been sent to your email for password reset'}, status=status.HTTP_200_OK)

class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)


            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Ivalid token, request a new one'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response(
                {'success': True, 'message': 'Valid credentials', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)


        except DjangoUnicodeDecodeError:
            return Response({'error': 'Ivalid token, request a new one'}, status=status.HTTP_401_UNAUTHORIZED)




