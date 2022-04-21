from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.user = User(username='ayzaq')
        self.user.save()
        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is test setup',user=self.user)


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='12moi', password='12moi@gmail.com')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
