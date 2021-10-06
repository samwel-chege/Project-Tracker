from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime as dt


class Cohort(models.Model):
    
    name=models.CharField(max_length=20, null=True)
    details = models.CharField(max_length=500, null=True, blank=True, default="A Moringa cohort.")

    @classmethod
    def get_cohorts(cls):
        all_cohorts = Cohort.objects.all()
        return all_cohorts

    def save_cohort(self):
        self.save()

    def __str__(self):
        return f'{self.name}'



class Language(models.Model):
    
    name=models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100, null=True, default="A programming language/framework.")

    @classmethod
    def get_languages(cls):
        all_languages = Language.objects.all()
        return all_languages

    def save_language(self):
        self.save()

    def __str__(self):
        return f'{self.name}'



class Profile(models.Model):
    
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)

    profile_pic = models.ImageField(upload_to='images/profiles/', blank=True, default = 0, null=True)
    bio = models.CharField(max_length=500, null=True, blank=True, default="bio")
    email = models.EmailField(blank=True, default="email", null=True)

    cohort=models.ForeignKey(Cohort, null=True, blank=True, on_delete=models.SET_NULL, related_name="student")

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def get_profiles(cls):
        all_profiles = Profile.objects.all()
        return all_profiles

    @classmethod
    def search_profile(cls, search_term):
        profile_found = Profile.objects.filter(title__icontains=search_term)
        return profile_found



class Project(models.Model):
    
    owner=models.ForeignKey(User,on_delete=models.CASCADE, related_name="my_project", null=True)
    cohort=models.ForeignKey(Cohort, null=True, on_delete=models.SET_NULL, related_name="project")
    language=models.ForeignKey(Language, null=True, on_delete=models.SET_NULL, related_name="project")

    member=models.ForeignKey(User, on_delete=models.SET_NULL, related_name="group_project", blank=True, null=True)

    title=models.CharField(max_length=30, null=True)
    project_image=models.ImageField(upload_to='images/projects/', blank=True, default = 0, null=True)
    description=models.TextField(max_length=320, blank=True, null=True)
    github_link=models.URLField(blank=True, null=True)

    date=models.DateField(auto_now=True, blank=True, null=True)


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
        