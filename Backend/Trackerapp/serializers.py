from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')

        return attrs
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=500)

    class Meta:
        model = CustomUser
        fields = ['token']

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255, min_length=3)
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    username=serializers.EmailField(max_length=68, min_length=3, read_only=True)
    tokens=serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model= CustomUser
        fields = ['email', 'username', 'password', 'tokens']
    def validate(self, attrs):
        email=attrs.get('email', '')
        password=attrs.get('password', '')

        user=auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Confirm if your credentials are valid')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled for inactivity')

        if not user.is_verified:
            raise AuthenticationFailed('Account not verified')



        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens(),
        }

        return super().validate(attrs)


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email=serializers.EmailField(min_length=3)


    class Meta:
        fields = ['email']  

    def validate(self, attrs):
        email = attrs['data'].get('email', '')
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64=urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user)
            current_site=get_current_site(
                request=attrs['data'].get('request')).domain
            relativeLink=reverse(
                'password-reset-confirmation', kwargs={'uidb64': uidb64, 'token': token})
            absoluteurl = 'http://'+current_site+relativeLink
            email_body='Hello, \n Click on the link below to reset your password  \n'+ absoluteurl
            data={'email_body':email_body,'to_email':user.email, 'email_subject':'Reset your password'}

            Util.send_email(data)
            
            return attrs
        return super().validate(attrs)