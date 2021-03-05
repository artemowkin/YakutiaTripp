import datetime

from django.test import TestCase

from ..serializers import NewsSerializer
from ..models import News


class NewsSerializerTest(TestCase):
    """Case of testing NewsSerializer"""

    def test_validate_correct_data(self):
        """Test: can serializer validate a correct data"""
        serializer = NewsSerializer(data={
            "title": "some news", "preview": "hello.png",
            "text": "something new"
        })

        self.assertTrue(serializer.is_valid())

    def test_validate_news_model_entry(self):
        """Test: can serializer validata a News model entry"""
        news = News.objects.create(
            title="some news", preview="hello.png", text="something new"
        )
        serializer = NewsSerializer(news)

        self.assertTrue(serializer.is_valid())

    def test_serializer_renders_correct_data(self):
        """Test: does serializer renders correct json data"""
        serializer = NewsSerializer(data={
            "title": "some news", "preview": "hello.png",
            "text": "something new"
        })

        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            serializer.validated_data, {
                'title': 'some news', 'preview': '/static/hello.png',
                'text': 'something new', 'pub_date': datetime.date.today()
            }
        )
