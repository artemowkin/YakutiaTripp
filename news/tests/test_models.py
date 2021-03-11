import uuid
import datetime

from django.test import TestCase
from django.db.utils import IntegrityError

from ..models import News


class NewsTest(TestCase):
    """Case of testing News model"""

    def setUp(self):
        self.news = News.objects.create(
            title="some news", preview="hello.png", text="something new"
        )

    def test_create_entry(self):
        """Test: does News model create an entry"""
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(News.objects.first(), self.news)

    def test_created_entry_fields(self):
        """Test: does News model create correct entry with correct fields"""
        self.assertEqual(self.news.title, 'some news')
        self.assertEqual(self.news.preview.url, '/media/hello.png')
        self.assertEqual(self.news.text, 'something new')
        self.assertEqual(self.news.pub_date, datetime.date.today())

    def test_string_representation(self):
        """Test: does News model entry __str__ return news title"""
        self.assertEqual(str(self.news), self.news.title)

    def test_pk_is_uuid(self):
        """Test: is model pk UUID field"""
        self.assertIsInstance(self.news.pk, uuid.UUID)

    def test_unique_title_constraint(self):
        """Test: is title unique"""
        with self.assertRaises(IntegrityError):
            second_news = News.objects.create(
                title="some news", preview="hello.png", text="something new"
            )
