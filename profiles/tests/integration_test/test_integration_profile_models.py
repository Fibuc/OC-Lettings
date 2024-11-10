from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


class profileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='usertest', password='12345!')
        self.profile = Profile.objects.create(user=self.user,favorite_city='New York')

    def test_cascade_when_user_delete(self):
        self.user.delete()
        self.assertEqual(Profile.objects.count(), 0)
        self.assertEqual(User.objects.count(), 0)

    def test_no_cascade_when_profile_delete(self):
        self.profile.delete()
        self.assertEqual(Profile.objects.count(), 0)
        self.assertEqual(User.objects.count(), 1)
