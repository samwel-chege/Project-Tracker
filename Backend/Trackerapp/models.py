from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime as dt


class Cohort(models.Model):
    
    name=models.CharField(max_length=15, null=True)
    code=models.CharField(max_length=10, null=True)

    details = models.CharField(max_length=500, null=True, blank=True, default="A Moringa class.")



class Profile(models.Model):
    
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)

    profile_pic = models.ImageField(upload_to='images/profiles/', blank=True, default = 0, null=True)
    bio = models.CharField(max_length=500, null=True, blank=True, default="bio")
    email = models.EmailField(blank=True, default="email", null=True)

    cohort=models.ForeignKey(Cohort, null=True, blank=True, on_delete=models.SET_NULL, related_name="student")



class Project(models.Model):
    
    owner=models.ForeignKey(User,on_delete=models.CASCADE, related_name="my_project", null=True)
    cohort=models.ForeignKey(Cohort, null=True, blank=True, on_delete=models.SET_NULL, related_name="project")

    member=models.ForeignKey(User, on_delete=models.SET_NULL, related_name="group_project", blank=True, null=True)

    title=models.CharField(max_length=30, null=True)
    project_image=models.ImageField(upload_to='images/projects/', blank=True, default = 0, null=True)
    description=models.TextField(max_length=320, blank=True, null=True)
    github_link=models.URLField(blank=True, null=True)

    date=models.DateField(auto_now=True, blank=True, null=True)
        