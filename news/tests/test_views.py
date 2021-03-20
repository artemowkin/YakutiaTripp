from django.test import TestCase
from django.urls import reverse

from ..models import News


class AllNewsViewTest(TestCase):
    """Case of testing AllNewsView"""

    def test_response_status_code(self):
        """Test: is view response has correct status code"""
        response = self.client.get(reverse('all_news'))
        self.assertEqual(response.status_code, 200)


class ConcreteNewsViewTest(TestCase):
    """Case of testing ConcreteNewsView"""

    def test_response_status_code(self):
        """Test: is view response has correct status code"""
        news = News.objects.create(
            title="some news", preview="hello.png", text="something new"
        )
        response = self.client.get(reverse('concrete_news', args=[news.pk]))
        self.assertEqual(response.status_code, 200)


class LastNewsViewTest(TestCase):
    """Case of testing LastNewsView"""

    def test_response_status_code(self):
        """Test: is view response has correct status code"""
        response = self.client.get(reverse('last_news'))
        self.assertEqual(response.status_code, 200)
