from django.test import TestCase
from main.models import Summary
from datetime import datetime

class ModelTests(TestCase):
    def test_model_summary(self):
        summary = Summary(url="http://www.example.com", title="example", paragraphs="This is a test", fetch_date=datetime.now())
        summary.save()
        summary = Summary.objects.get(url="http://www.example.com")
        self.assertEqual(summary.url, "http://www.example.com")
