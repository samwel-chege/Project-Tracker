from django.test import TestCase
from .models import *
from Trackerapp.models import CustomUser,Student
from django.contrib.auth import get_user_model

# Create your tests here.
class UsersManagersTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='fredrick@g.com', password = 'trackerapp123')
        self.assertEqual(user.email, 'fredrick@g.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="trackerapp123")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='wambua@g.com', password='projecttracker123')
        self.assertEqual(admin_user.email, 'wambua@g.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='wambua@g.com', password='projecttracker', is_superuser=False)
    


class CohortTestClass(TestCase):
    
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.core1 = Cohort.objects.create(name='core1')

    def test_save_cohort(self):
        '''
        test case to save a test cohort.
        '''
        self.core1.save_cohort()
        self.assertTrue(isinstance(self.core1, Cohort))

    def test_get_cohorts(self):
        '''
        test case to check if cohort was saved.
        '''
        cohorts = Cohort.get_cohorts()
        self.assertTrue(len(cohorts) > 0)


class DevStyleTestClass(TestCase):
    
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.django = DevStyle.objects.create(name='django')

    def test_save_style(self):
        '''
        test case to save a test development style.
        '''
        self.django.save_style()
        self.assertTrue(isinstance(self.django, DevStyle))

    def test_get_styles(self):
        '''
        test case to check if the DevStyle was saved.
        '''
        styles = DevStyle.get_styles()
        self.assertTrue(len(styles) > 0)


class StudentTestClass(TestCase):

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.student = Student(id = 1)

    def test_instance(self):
        '''
        test case to test if 'isinstance'.
        '''
        self.assertTrue(isinstance(self.student, Student)) 

    def test_get_students(self):
        '''
        test case to save a test student profile and check if it is saved.
        '''
        self.student.save_student_profile(self)
        students = Student.get_students()
        self.assertTrue(len(students)>0)
    
    def test_delete_student(self):
        '''
        test case to delete a test student.
        '''
        self.student.delete()
        students = Student.get_students()
        self.assertTrue(len(students)<1)


class ProjectTestClass(TestCase):

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.Projo = Project.objects.create(title='Projo')

    def test_save_project(self):
        '''
        test case to save a test project.
        '''
        self.Projo.save_project()
        self.assertTrue(isinstance(self.Projo, Project))

    def test_all_projects(self):
        '''
        test case to check if project has been saved.
        '''
        projects = Project.all_projects()
        self.assertTrue(len(projects) > 0)

