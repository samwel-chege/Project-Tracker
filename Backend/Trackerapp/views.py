import os
import json
from decouple import config, Csv
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.templatetags.static import static
from django.http  import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.http  import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.defaulttags import register

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from .models import *

# Create your views here.

def home(request):
    current_user = request.user
    profiles = Profile.get_profiles()
    projects = Project.all_projects()
    cohorts = Cohort.get_cohorts()
    languages = Language.get_languages()

    return render(request, 'home.html',{"projects":projects, "profiles": profiles, "cohorts":cohorts, "languages": languages})


@login_required(login_url='/accounts/login/')
def profile(request, username):
    current_user = request.user
    projects = Project.objects.filter(owner=current_user)

    return render(request, 'profile.html', {"projects":projects,"current_user":current_user})


@login_required(login_url='/accounts/login/')
def cohort(request, name):
    cohort = Cohort.objects.get(name=name)
    
    return render(request, 'cohort.html', {'cohort':cohort})


@login_required(login_url='/accounts/login/')
def project(request, title):
    project = Project.objects.get(title=title)
    
    return render(request, 'project.html', {'project':project})


@login_required(login_url='/accounts/login/')
def language(request, name):
    language = Language.objects.get(name=name)
    
    return render(request, 'language.html', {'language':langauge})


def all_profiles(request):
    current_user = request.user
    profiles = Profile.get_profiles()

    return render(request, 'all_profiles.html',{"profiles": profiles})


def all_projects(request):
    current_user = request.user
    projects = Project.all_projects()

    return render(request, 'all_projects.html',{"projects": projects})
