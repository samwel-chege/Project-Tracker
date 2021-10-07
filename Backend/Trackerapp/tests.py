#from django.test import TestCase
import unittest
import models
#from . models import *


class CohortTestClass(TestCase):
    
    def setUp(self):
        self.core1 = Cohort.objects.create(name='core1')

    def test_instance(self):
        self.core1.save_cohort()
        self.assertTrue(isinstance(self.core1, Cohort))

    def test_get_cohorts(self):
        cohorts = Cohort.get_cohorts()
        self.assertTrue(len(cohorts) > 0)


class LanguageTestClass(TestCase):
    
    def setUp(self):
        self.django = Language.objects.create(name='django')

    def test_instance(self):
        self.django.save_language()
        self.assertTrue(isinstance(self.django, Language))

    def test_get_languages(self):
        languages = Language.get_languages()
        self.assertTrue(len(languages) > 0)


class StudentTestClass(TestCase):

    def setUp(self):
        self.student = Student(id = 1, name='TestUser')

    def test_instance(self):
        self.assertTrue(isinstance(self.student, Student)) 

    def test_save_student_profile(self):
        self.student.save_student_profile()
        students = Student.get_students()
        self.assertTrue(len(students)>0)
    
    def test_delete_student(self):
        self.student.delete()
        students = Student.get_students()
        self.assertTrue(len(students)<1)


class ProjectTestClass(TestCase):

    def setUp(self):
        self.Projo = Project.objects.create(title='Projo')

    def test_instance(self):
        self.Projo.save_project()
        self.assertTrue(isinstance(self.Projo, Project))

    def test_all_projects(self):
        projects = Project.all_projects()
        self.assertTrue(len(projects) > 0)