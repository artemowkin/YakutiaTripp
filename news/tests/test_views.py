import simplejson as json

from django.test import TestCase
from django.urls import reverse
from rest_framework.renderers import JSONRenderer

from ..serializers import NewsSerializer
from ..models import News


class AllNewsViewTest(TestCase):
    """Case of testing AllNewsView"""

    def test_response_status_code(self):
        """Test: is view response has correct status code"""
        response = self.client.get(reverse('all_news'))
        self.assertEqual(response.status_code, 200)

    def test_response_has_correct_data(self):
        """Test: has response correct serialized news"""
        news = News.objects.create(
            title="some news", preview="test.png", text="something new"
        )
        response = self.client.get(reverse('all_news'))
        response_json = json.loads(response.content)

        self.assertEqual(len(response_json), News.objects.count())
