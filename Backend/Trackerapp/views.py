from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from rest_framework import generics, serializers, status
from rest_framework.response import Response

from .models import *
from .serializers import RegisterSerializer

from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from .permissions import *


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
        permission_classes = (IsAdminOrReadOnly,)
        user = request.data
        serializer =self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        user_data =serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class StudentView(APIView):

    def get(self, request, format=None):
        all_students = Student.objects.all()
        serializers = StudentSerializer(all_students, many=True)

        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = StudentSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectView(APIView):

    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
            
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class CohortView(APIView):
    
    def get(self, request, format=None):
        all_cohorts = Cohort.objects.all()
        serializers = CohortSerializer(all_cohorts, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = CohortSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
            
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class StyleView(APIView):
    
    def get(self, request, format=None):
        all_styles = DevStyle.objects.all()
        serializers = StyleSerializer(all_styles, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = StyleSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
            
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentProfile(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_student(self, pk):
        try:
            return Student.objects.get(pk=pk)

        except Student.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        student = self.get_student(pk)
        serializers = StudentSerializer(student)
        return Response(serializers.data)


class ProjectDevModeView(APIView):
    def get_style(self, pk):
        try:
            return DevStyle.objects.get(pk=pk)

        except DevStyle.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        style = self.get_style(pk)
        project = style.project
        serializers = DevStyleSerializer(project, many=True)
        return Response(serializers.data)


class CohortMembersView(APIView):
    def get_cohort(self, pk):
        try:
            return Cohort.objects.get(pk=pk)

        except Cohort.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        cohort = self.get_cohort(pk)
        student = cohort.student
        serializers = StudentSerializer(student, many=True)
        return Response(serializers.data)