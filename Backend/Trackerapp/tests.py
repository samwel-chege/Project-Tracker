from django.test import TestCase
from Trackerapp.models import CustomUser
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
                email='wambua@g.com', password='thatsmycar', is_superuser=False)
    