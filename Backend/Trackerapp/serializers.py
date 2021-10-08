from rest_framework import serializers
from .models import *

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
        fields = ('user', 'bio', 'profile_pic', 'email', 'cohort', 'projects_owned', 'is_scrum', 'member')

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
        fields = ('name', 'details', 'style')

    def create(self, validated_data):
        return Cohort(**validated_data)


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevStyle
        fields = ('name', 'description')

    def create(self, validated_data):
        return DevStyle(**validated_data)

