from django.db.models import fields
from rest_framework import serializers

from .models import *

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



class StudentSerializer(serializers.ModelSerializer):
    projects_owned = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    is_scrum = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    is_dev = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    cohort = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Student
        fields = ('id', 'user', 'bio', 'profile_pic', 'email', 'cohort', 'projects_owned', 'is_scrum', 'is_dev')

    def create(self, validated_data):
        return Student(**validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    # owner = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='email'
    # )

    # scrum = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='email'
    # )

    # member = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='email'
    # )

    cohort = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    style = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Project
        fields = ('id', 'title', 'project_image', 'description', 'owner', 'scrum', 'member', 'cohort', 'style', 'github_link', 'date')

    def create(self, validated_data):
        return Project(**validated_data)


class CohortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cohort
        fields = ('id', 'name', 'details')

    def create(self, validated_data):
        return Cohort(**validated_data)


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevStyle
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        return DevStyle(**validated_data)


class NewProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title', 'project_image', 'description', 'owner', 'scrum', 'cohort', 'style', 'github_link', 'date')

    def create(self, validated_data):
        return Project(**validated_data)


class NewStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'profile_pic', 'cohort', 'email', 'bio')

    def create(self, validated_data):
        return Student(**validated_data)


class NewCohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = ('id', 'name', 'details')

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

