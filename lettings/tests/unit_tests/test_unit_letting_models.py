from django.test import TestCase
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting
from conftest import address


class AddressModelTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(**address)

    def test_address_creation(self):
        self.assertIsInstance(self.address, Address)
        self.assertEqual(self.address.number, address['number'])
        self.assertEqual(self.address.street, address['street'])
        self.assertEqual(self.address.city, address['city'])
        self.assertEqual(self.address.state, address['state'])
        self.assertEqual(self.address.zip_code, address['zip_code'])
        self.assertEqual(self.address.country_iso_code, address['country_iso_code'])

    def test_str_method(self):
        self.assertEqual(str(self.address), f"{self.address.number} {self.address.street}")

    def test_number_max_value_validation(self):
        self.address.number = 10000
        with self.assertRaises(ValidationError):
            self.address.full_clean()

    def test_state_length_validation(self):
        self.address.state = "S"
        with self.assertRaises(ValidationError):
            self.address.full_clean()

    def test_zip_code_max_value_validation(self):
        self.address.zip_code = 100000
        with self.assertRaises(ValidationError):
            self.address.full_clean()

    def test_country_iso_code_length_validation(self):
        self.address.country_iso_code = "US"
        with self.assertRaises(ValidationError):
            self.address.full_clean()


class LettingModelTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(**address)
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_letting_creation(self):
        self.assertIsInstance(self.letting, Letting)
        self.assertIsInstance(self.letting.address, Address)
        self.assertEqual(self.letting.title, "Test Letting")
        self.assertEqual(self.letting.address, self.address)

    def test_letting_str_method(self):
        self.assertEqual(str(self.letting), self.letting.title)
