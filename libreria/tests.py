from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='normal',
                                                   email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)