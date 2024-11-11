from django.test import Client, TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User
import pytest


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='usertest', password='12345!')
        self.profile = Profile.objects.create(user=self.user, favorite_city='New York')

    def test_letting_index_view(self):
        path = reverse('profiles:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")

    @pytest.mark.django_db
    def test_letting_view(self):
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        content = response.content.decode()
        expected_title = f"<title>{self.user.username}</title>"
        expected_content = f"<p><strong>First name :</strong> {self.profile.user.first_name}</p>"  # noqa: E231, E203, E501
        self.assertIn(expected_title, content)
        self.assertIn(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
