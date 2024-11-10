from django.test import TestCase
from django.urls import reverse, resolve
from lettings.models import Letting, Address
from conftest import address
import pytest


class TestUrls(TestCase):
    def test_index_url(self):
        path = reverse('lettings:index')
        self.assertEqual(path, '/lettings/')
        self.assertEqual(resolve(path).view_name, 'lettings:index')

    @pytest.mark.django_db
    def test_letting_url(self):
        Address.objects.create(**address)
        letting = Letting.objects.create(title='title_test', address=Address.objects.first())
        path = reverse('lettings:letting', args=[letting.pk])
        self.assertEqual(path, f"/lettings/{letting.pk}/")
        self.assertEqual(resolve(path).view_name, 'lettings:letting')
