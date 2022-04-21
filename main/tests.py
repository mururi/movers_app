from django.test import TestCase

# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.user = User(username='ayzaq')
        self.user.save()
        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is test setup',user=self.user)