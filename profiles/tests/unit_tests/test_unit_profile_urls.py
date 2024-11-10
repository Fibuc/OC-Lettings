from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile
import pytest


class TestUrls(TestCase):

    def test_index_url(self):
        path = reverse('profiles:index')
        self.assertEqual(path, '/profiles/')
        self.assertEqual(resolve(path).view_name, 'profiles:index')

    @pytest.mark.django_db
    def test_profile_url(self):
        User.objects.create(username='usertest', password='Abc1234!')
        user = User.objects.first()
        Profile.objects.create(user=user, favorite_city='New York')
        path = reverse('profiles:profile', args=[user.username])
        self.assertEqual(path, f'/profiles/{user.username}/')
        self.assertEqual(resolve(path).view_name, 'profiles:profile')
