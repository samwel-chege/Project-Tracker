from django.test import TestCase
from Trackerapp.models import CustomUser
from django.contrib.auth import get_user_model

# Create your tests here.
class UsersManagersTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='freddy@g.com', password = 'drovehomesave')
        self.assertEqual(user.email, 'freddy@g.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)