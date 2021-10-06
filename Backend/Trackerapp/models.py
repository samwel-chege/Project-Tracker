from django.db import models
from django.test import TestCase
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from cloudinary.models import CloudinaryField


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if email is None:
            raise ValueError('Users must have an email')

        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):

        if password is None:
            raise ValueError('Password should not be none')

        user=self.create_user(email, password)
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
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Cohort(models.Model):
    
    name=models.CharField(max_length=15, null=True)
    code=models.CharField(max_length=10, null=True)
    details = models.CharField(max_length=500, null=True, blank=True, default="A Moringa class.")

    @classmethod
    def get_cohorts(cls):
        all_cohorts = Cohort.objects.all()
        return all_cohorts
    def save_cohort(self):
        self.save()
    def __str__(self):
        return f'{self.name}'



class Student(models.Model):
    name = models.CharField(max_length=70)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name= 'student')
    cohort = models.ForeignKey(Cohort, on_delete=models.SET_NULL, null=True, blank=True)

    @classmethod
    def get_students(cls):
        all_students = Student.objects.all()
        return all_students

    def save_student(self):
        self.save()
    
    def __str__(self):
        return f'{self.name}'


