from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, Token
from .models import *
from rest_framework_simplejwt.tokens import Token
from .models import CustomUser, Student, Project, Cohort, DevStyle
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode



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



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'bio', 'profile_pic', 'email', 'cohort', 'projects_owned', 'is_scrum', 'is_dev')

    def create(self, validated_data):
        return Student(**validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'project_image', 'description', 'owner', 'scrum', 'member', 'cohort', 'style', 'github_link', 'date')

    def create(self, validated_data):
        return Project(**validated_data)


class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = ('name', 'details')

    def create(self, validated_data):
        return Cohort(**validated_data)


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevStyle
        fields = ('name', 'description')

    def create(self, validated_data):
        return DevStyle(**validated_data)


class NewProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'project_image', 'description', 'owner', 'scrum', 'cohort', 'style', 'github_link', 'date')

    def create(self, validated_data):
        return Project(**validated_data)


class NewStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'profile_pic', 'cohort', 'email', 'bio')

    def create(self, validated_data):
        return Student(**validated_data)


class NewCohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = ('name', 'details')

    def create(self, validated_data):
        return Cohort(**validated_data)

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
    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']  


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The password reset link is invalid', 401)

            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            raise AuthenticationFailed('The password reset link is invalid', 401)

        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'invalid_token': ('Token is expired or invalid')

    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('invalid_token')