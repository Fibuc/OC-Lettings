from django.test import Client
from django.test import TestCase
from django.urls import reverse


class OCLettingTestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        content = response.content.decode()
        expected_content = 'Welcome to Holiday Homes'
        self.assertIn(expected_content, content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_404_view(self):
        response = self.client.get('/bad_url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_500_view(self):
        response = self.client.get(reverse('500'))
        self.assertEqual(response.status_code, 500)
        