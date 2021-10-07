from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from rest_framework import generics, serializers, status
from rest_framework.response import Response

from .models import CustomUser
from .serializers import RegisterSerializer




# Create your views here.

# def signup(request):
#     if request.method == 'POST':     
#         form = SignUpForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Hi {username} Your account was created successfully. ')
#             return redirect('login')
#     else:
#         form = SignUpForm

#     return render(request, 'registration/signup.html', {'form':form,'registered': False } )

# Serializer class view
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()
    def post(self, request):
        user = request.data
        serializer =self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        user_data =serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)