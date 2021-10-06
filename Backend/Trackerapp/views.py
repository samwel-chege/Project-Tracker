from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Trackerapp.forms import *
from django.shortcuts import get_object_or_404, render,redirect, resolve_url




# Create your views here.

def signup(request):
    if request.method == 'POST':     
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} Your account was created successfully. ')
            return redirect('login')
    else:
        form = SignUpForm

    return render(request, 'registration/signup.html', {'form':form,'registered': False } )