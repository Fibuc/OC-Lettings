from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='usertest', password='12345!')
        self.profile = Profile.objects.create(user=self.user, favorite_city='New York')

    def test_profile_creation(self):
        self.assertIsInstance(self.profile, Profile)
        self.assertIsInstance(self.profile.user, User)
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.favorite_city, "New York")

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile), self.profile.user.username)
