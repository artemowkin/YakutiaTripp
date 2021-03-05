import datetime

from django.test import TestCase

from ..models import News


class NewsTest(TestCase):
    """Case of testing News model"""

    def test_create_entry_fields(self):
        """Test: does News model create an entry"""
        news = News.objects.create(
            title="some news", preview="hello.png", text="something new"
        )

        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(News.objects.first(), news)

    def test_create_entry(self):
        """Test: does News model create correct entry with correct fields"""
        news = News.objects.create(
            title="some news", preview="hello.png", text="something new"
        )

        self.assertEqual(news.title, 'some news')
        self.assertEqual(news.preview.url, '/media/hello.png')
        self.assertEqual(news.text, 'something new')
        self.assertEqual(news.pub_date, datetime.date.today())

    def test_string_representation(self):
        """Test: does News model entry __str__ return news title"""
        news = News.objects.create(
            title="some news", preview="hello.png", text="something new"
        )

        self.assertEqual(str(news), news.title)
