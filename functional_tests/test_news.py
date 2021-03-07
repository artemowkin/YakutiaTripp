import datetime
import simplejson as json

from django.test import LiveServerTestCase
from django.urls import reverse

from news.models import News
from news.serializers import NewsSerializer


class NewsEndpointsTest(LiveServerTestCase):
    """Test of news endpoints"""

    def setUp(self):
        self.news = News.objects.create(
            title="some news", preview="test.png", text="something new"
        )
        self.serialized_news = NewsSerializer(self.news)

    def test_api_news_endpint_returns_correct_data(self):
        """Test: does /api/news/ endpoint return correct data"""
        response = self.client.get(reverse('all_news'))
        response_json = json.loads(response.content)

        self.assertEqual(len(response_json), News.objects.count())
        self.assertEqual(response_json[0], {
            'pk': str(self.news.pk), 'title': 'some news',
            'preview': '/media/test.png', 'text': 'something new',
            'pub_date': datetime.date.today().isoformat()
        })

    def test_api_news_for_concrete_news_endpoint_returns_correct_data(self):
        """Test: does /api/news/{news_pk}/ endpoint return correct data"""
        response = self.client.get(
            reverse('concrete_news', args=[self.news.pk])
        )
        response_json = json.loads(response.content)

        self.assertEqual(response_json, {
            'pk': str(self.news.pk), 'title': 'some news',
            'preview': '/media/test.png', 'text': 'something new',
            'pub_date': datetime.date.today().isoformat()
        })

    def test_api_news_last_endpoint_returns_correct_data(self):
        """Test: does /api/news/last/ endpoint return correct data"""
        for i in range(9):
            News.objects.create(
                title=f"some news {i}", preview="test.png",
                text="something new"
            )

        response = self.client.get(reverse('last_news'))
        response_json = json.loads(response.content)

        self.assertEqual(len(response_json), 9)
        self.assertIn({
            'pk': str(self.news.pk), 'title': 'some news',
            'preview': '/media/test.png', 'text': 'something new',
            'pub_date': datetime.date.today().isoformat()
        }, response_json)
