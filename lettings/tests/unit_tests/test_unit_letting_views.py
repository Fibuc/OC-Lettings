from django.test import Client, TestCase
from django.http import Http404 
from django.urls import reverse
from lettings.models import Letting, Address
from conftest import address
import pytest


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(**address)
        self.letting = Letting.objects.create(address=self.address, title='test_title')

    def test_letting_index_view(self):
        path = reverse('lettings:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")

    @pytest.mark.django_db
    def test_letting_view_success(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.pk]))
        content = response.content.decode()
        expected_title = f"<title>{self.letting.title}</title>"
        expected_content = f"<p>{self.address.number} {self.address.street}</p>"
        self.assertIn(expected_title, content)
        self.assertIn(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")

    @pytest.mark.django_db
    def test_letting_view_bad_id(self):
        response = self.client.get(reverse('lettings:letting', args=[999]))
        self.assertRaises(Http404)
        self.assertEqual(response.status_code, 404)
