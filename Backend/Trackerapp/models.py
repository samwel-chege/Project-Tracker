from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from project import settings

import datetime as dt


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if username is None:
            raise ValueError('Users must have a username')

        if password is None:
            raise ValueError('Password should not be none')

        if email is None:
            raise ValueError('Users must have an email')

        user=self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):

        if username is None:
            raise ValueError('Users must have a username')

        if password is None:
            raise ValueError('Password should not be none')

        if email is None:
            raise ValueError("User must have an email")

        user=self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    objects = UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        return ''



class DevStyle(models.Model):
    '''
    DevStyle class to define the project development style
    '''
    
    name=models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100, null=True, default="A development style.")

    def create(self, validated_data):
        return DevStyle.objects.create(**validated_data)

    @classmethod
    def get_styles(cls):
        all_styles = DevStyle.objects.all()
        return all_styles

    def save_style(self):
        self.save()

    def __str__(self):
        return f'{self.name}'



class Cohort(models.Model):
    '''
    Cohort class to define Cohort objects
    '''
    
    name=models.CharField(max_length=20, null=True)
    details = models.CharField(max_length=100, null=True, blank=True, default="A Moringa cohort.")

    style=models.ForeignKey(DevStyle, null=True, on_delete=models.SET_NULL, related_name="cohort")

    @classmethod
    def get_cohorts(cls):
        all_cohorts = Cohort.objects.all()
        return all_cohorts
    
    def create(self, validated_data):
        return Cohort.objects.create(**validated_data)

    def save_cohort(self):
        self.save()

    def __str__(self):
        return f'{self.name}'



class Student(models.Model):
    '''
    Student class to define student objects
    '''
    
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student", null=True)

    profile_pic = models.ImageField(upload_to='images/profiles/', blank=True, default = 0, null=True)
    bio = models.CharField(max_length=500, null=True, blank=True, default="A student at Moringa School.")
    email = models.EmailField(blank=True, default="N/A", null=True)

    cohort=models.ForeignKey(Cohort, null=True, blank=True, on_delete=models.SET_NULL, related_name="student")

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_student_profile(sender, instance, created, **kwargs):
        if created:
            Student.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def save_student_profile(sender, instance, **kwargs):
        instance.student.save()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    @classmethod
    def get_students(cls):
        all_students = Student.objects.all()
        return all_students

    @classmethod
    def search_student(cls, search_term):
        student_found = Student.objects.filter(title__icontains=search_term)
        return student_found



class Project(models.Model):
    '''
    Project class to define project objects
    '''
    
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="my_project", null=True)
    cohort=models.ForeignKey(Cohort, null=True, on_delete=models.SET_NULL, related_name="project")
    style=models.ForeignKey(DevStyle, null=True, on_delete=models.SET_NULL, related_name="project")

    scrum=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="scrum", blank=True, null=True)
    member=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="member", blank=True, null=True)
    #dev1=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="dev1", blank=True, null=True)
    #dev2=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="dev2", blank=True, null=True)
    #dev3=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="dev3", blank=True, null=True)
    #dev4=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="dev4", blank=True, null=True)
    #dev5=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="dev5", blank=True, null=True)
    #dev6=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="dev6", blank=True, null=True)
    #dev7=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="dev7", blank=True, null=True)
    #dev8=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="dev8", blank=True, null=True)

    title=models.CharField(max_length=30, null=True)
    project_image=models.ImageField(upload_to='images/projects/', blank=True, default = 0, null=True)
    description=models.TextField(max_length=320, blank=True, null=True)
    github_link=models.URLField(blank=True, null=True)

    date=models.DateField(auto_now=True, blank=True, null=True)


    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, search_term):
        search_results = Project.objects.filter(title__icontains=search_term)
        return search_results

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    @classmethod
    def get_project_by_id(cls, id):
        project_found = cls.objects.get(pk=id)
        return project_found

    # @classmethod
    # def get_projects_by_style(cls, style):
    #     project_found = cls.objects.get(pk=style)
    #     return project_by_style

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.title}'
        

