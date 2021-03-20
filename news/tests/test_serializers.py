import datetime

from django.test import TestCase

from ..serializers import NewsSerializer
from ..models import News


class NewsSerializerTest(TestCase):
    """Case of testing NewsSerializer"""

    def test_correct_serializing_news_model_entry(self):
        """Test: can serializer serialize a News model entry"""
        news = News.objects.create(
            title="some news", preview='hello.png', text="something new"
        )
        serializer = NewsSerializer(news)

        self.assertEqual(serializer.data, {
            'pk': str(news.pk), 'title': 'some news',
            'preview': '/media/hello.png', 'text': 'something new',
            'pub_date': datetime.date.today().isoformat()
        })
