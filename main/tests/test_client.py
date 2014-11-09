from django.test import Client
from django.test import TestCase

client = Client()
class ClientTests(TestCase):
    def test_url_post(self):
        response = client.post('/', {'url': 'http://www.example.com'})
        self.assertEqual(response.status_code, 302)
