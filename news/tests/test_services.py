from django.test import TestCase

from ..services import GetNewsService
from ..models import News


class GetNewsServiceTest(TestCase):
    """Service to get all news entries"""

    def setUp(self):
        self.service = GetNewsService()

    def test_get_all_returns_all_entries(self):
        """Test: get_all method returns all news entries"""
        news = News.objects.create(
            title="something new", preview="hello.png", text="some text"
        )
        all_entries = self.service.get_all()

        self.assertEqual(all_entries.count(), News.objects.count())
        self.assertEqual(all_entries[0], news)
