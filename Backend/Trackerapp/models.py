from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from cloudinary.models import CloudinaryField
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
#from django.db.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
from project import settings
import datetime as dt
from django.db.models.deletion import CASCADE
import django_filters
from django.db.models.fields import SlugField
# from autoslug import AutoSlugField

# Create your models here.

# Custom usermanager class start
class UserManager(BaseUserManager):
    def create_user(self, username, email, password):

        if username is None:
            raise ValueError('Users must have a username')

        if password is None:
            raise ValueError('Password should not be none')

        if email is None:
            raise ValueError('Users must have an email')

        user=self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, username, password, **kwargs):

        if username is None:
            raise ValueError('Users must have a username')

        if password is None:
            raise ValueError('Password should not be none')

        if email is None:
            raise ValueError("User must have an email")

        user=self.create_user(username, email, password, **kwargs)

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


# customuser class start
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    objects = UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

# customuser class end

class Cohort(models.Model):
    '''
    Cohort class to define Cohort objects
    '''
    
    name=models.CharField(max_length=20, null=True)
    details = models.CharField(max_length=100, null=True, blank=True, default="A Moringa cohort.")

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



class DevStyle(models.Model):
    '''
    DevStyle class to define the project development style
    '''
    
    name=models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100, null=True, default="A programming language/style.")

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



class Student(models.Model):
    '''
    Student class to define student objects
    '''

    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile", null=True)
    first_name = models.CharField(max_length=20, default="", blank=True, null=True,)
    surname = models.CharField(max_length=40, default="", blank=True, null=True,)

    profile_pic = CloudinaryField('image', blank=True, default = 0, null=True)
    cohort=models.ForeignKey(Cohort, null=True, blank=True, on_delete=models.SET_NULL, related_name="students")
    email = models.EmailField(blank=True, default="N/A", null=True)

    bio = models.CharField(max_length=500, null=True, blank=True, default="A student at Moringa School.")

    github_profile=models.URLField(blank=True, null=True)


    def __str__(self):
        return f'{self.user.username}'


    @receiver(post_save, sender=settings.AUTH_USER_MODEL)


    def create_student_profile(sender, instance, created, **kwargs):
        if created:
            Student.objects.create(user=instance)


    @receiver(post_save, sender=settings.AUTH_USER_MODEL)

 
    def save_student_profile(sender, instance, **kwargs):
        instance.profile.save()

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
    
    title=models.CharField(max_length=30, null=True)
    owner=models.ForeignKey(Student,on_delete=models.CASCADE, related_name="projects_owned", null=True)
    style=models.ForeignKey(DevStyle, blank=True, null=True, on_delete=models.SET_NULL, related_name="projects")
    cohort=models.ForeignKey(Cohort, blank=True, null=True, on_delete=models.SET_NULL, related_name="projects")

    project_image=CloudinaryField('image', blank=True, default = 0, null=True)
    github_link=models.URLField(blank=True, null=True)
    description=models.TextField(max_length=320, blank=True, null=True)

    date=models.DateField(auto_now=True, blank=True, null=True)
    members=models.ManyToManyField(Student, related_name="is_dev", blank=True)


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

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.title}'
        

