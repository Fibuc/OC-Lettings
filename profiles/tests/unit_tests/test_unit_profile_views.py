from django.test import Client, TestCase
from django.http import Http404
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User
import pytest


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='usertest', password='12345!')
        self.profile = Profile.objects.create(user=self.user, favorite_city='New York')

    def test_profile_index_view(self):
        path = reverse('profiles:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")

    @pytest.mark.django_db
    def test_profile_view(self):
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        content = response.content.decode()
        expected_title = f"<title>{self.user.username}</title>"
        expected_content = f"<p><strong>First name :</strong> {self.profile.user.first_name}</p>"  # noqa: E231, E203, E501
        self.assertIn(expected_title, content)
        self.assertIn(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    @pytest.mark.django_db
    def test_profile_view_bad_id(self):
        response = self.client.get(reverse('profiles:profile', args=['bad_username']))
        self.assertRaises(Http404)
        self.assertEqual(response.status_code, 404)
