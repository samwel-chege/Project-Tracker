from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from django.http import Http404

from rest_framework import generics, serializers, status, filters
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .permissions import *

import django_filters


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


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = ['cohort', 'style', 'owner']


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['cohort',]


class CohortsView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_cohorts = Cohort.objects.all()
        serializers = CohortSerializer(all_cohorts, many=True)

        return Response(serializers.data)


class StylesView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_styles = DevStyle.objects.all()
        serializers = StyleSerializer(all_styles, many=True)

        return Response(serializers.data)


class StudentProfileView(APIView):
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


class ProjectProfileView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)

        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)


class CohortProfileView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_cohort(self, pk):
        try:
            return Cohort.objects.get(pk=pk)

        except Cohort.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        cohort = self.get_cohort(pk)
        serializers = CohortSerializer(cohort)
        return Response(serializers.data)


class StyleProfileView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_style(self, pk):
        try:
            return DevStyle.objects.get(pk=pk)

        except DevStyle.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        style = self.get_style(pk)
        serializers = StyleSerializer(style)
        return Response(serializers.data)


class ProjectsByDevStyleView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_style(self, pk):
        try:
            return DevStyle.objects.get(pk=pk)

        except DevStyle.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        style = self.get_style(pk)
        project = style.project
        serializers = ProjectSerializer(project, many=True)
        return Response(serializers.data)


class ProjectsByCohortView(APIView):
    def get_cohort(self, pk):
        try:
            return Cohort.objects.get(pk=pk)

        except Cohort.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        cohort = self.get_cohort(pk)
        project = cohort.project
        serializers = ProjectSerializer(project, many=True)
        return Response(serializers.data)


class NewProjectView(APIView):
    serializer_class = NewProjectSerializer

    def post(self, request, format=None):
        serializers = NewProjectSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
            
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class NewStudentView(APIView):
    serializer_class = NewStudentSerializer

    def post(self, request, format=None):
        serializers = NewStudentSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class NewCohortView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = NewCohortSerializer

    def post(self, request, format=None):
        serializers = NewCohortSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentSearch(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'email']


class ProjectSearch(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'owner__user__username']