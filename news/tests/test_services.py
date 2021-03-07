import datetime

from django.test import TestCase

from ..services import GetNewsService
from ..models import News


class GetNewsServiceTest(TestCase):
    """Service to get all news entries"""

    def setUp(self):
        self.service = GetNewsService()
        self.news = News.objects.create(
            title="something new", preview="hello.png", text="some text"
        )

    def test_get_all_returns_all_entries(self):
        """Test: get_all method returns all news entries"""
        all_entries = self.service.get_all()

        self.assertEqual(all_entries.count(), News.objects.count())
        self.assertEqual(all_entries[0], self.news)

    def test_get_concrete_returns_a_concrete_entry(self):
        """Test: get_concrete method returns a concrete news entry"""
        entry = self.service.get_concrete(self.news.pk)

        self.assertEqual(entry, self.news)

    def test_get_last_returns_last_9_entries(self):
        """Test: does get_last method return last 9 news"""
        for i in range(1, 10):
            News.objects.create(
                title=f"news {i}", preview="hello.png", text="some text",
                pub_date=datetime.date.today()+datetime.timedelta(days=i)
            )

        entries = self.service.get_last()

        self.assertEqual(entries.count(), 9)
