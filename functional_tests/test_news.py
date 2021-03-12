import datetime

import requests
from django.test import LiveServerTestCase

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
        response = requests.get(self.live_server_url + '/api/news/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), News.objects.count())
        self.assertEqual(response.json()[0], {
            'pk': str(self.news.pk), 'title': 'some news',
            'preview': '/media/test.png', 'text': 'something new',
            'pub_date': datetime.date.today().isoformat()
        })

    def test_api_news_for_concrete_news_endpoint_returns_correct_data(self):
        """Test: does /api/news/{news_pk}/ endpoint return correct data"""
        response = requests.get(
            self.live_server_url + f'/api/news/{self.news.pk}/'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
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

        response = requests.get(self.live_server_url + '/api/news/last/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 9)
        self.assertIn({
            'pk': str(self.news.pk), 'title': 'some news',
            'preview': '/media/test.png', 'text': 'something new',
            'pub_date': datetime.date.today().isoformat()
        }, response.json())
