from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Letting, Address
from conftest import address


class TestLetting(TestCase):

    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(**address)
        self.letting = Letting.objects.create(address=self.address, title='test_title')

    def test_cascade_when_address_delete(self):
        self.address.delete()
        self.assertEqual(Letting.objects.count(), 0)
        self.assertEqual(Address.objects.count(), 0)

    def test_no_cascade_when_address_delete(self):
        self.letting.delete()
        self.assertEqual(Letting.objects.count(), 0)
        self.assertEqual(Address.objects.count(), 1)
