import datetime
import simplejson as json

from django.test import LiveServerTestCase
from django.urls import reverse

from news.models import News
from news.serializers import NewsSerializer


class TestNewsGetAllEndpoint(LiveServerTestCase):

    def setUp(self):
        self.news = News.objects.create(
            title="some news", preview="test.png", text="something new"
        )
        self.serialized_news = NewsSerializer(self.news)

    def test_api_news_endpint_returns_correct_data(self):
        """Test: Does /api/news/ endpoint return correct data"""
        response = self.client.get(reverse('all_news'))
        response_json = json.loads(response.content)

        self.assertEqual(response_json[0], {
            'title': 'some news', 'preview': '/media/test.png',
            'text': 'something new',
            'pub_date': datetime.date.today().isoformat()
        })
