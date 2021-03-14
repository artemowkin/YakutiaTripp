from django.test import TestCase
from django.urls import reverse


class AllReviewsViewTest(TestCase):
    """Case of testing AllReviewsView"""

    def test_response_status_code(self):
        """Test: is view response has correct status code"""
        response = self.client.get(reverse('all_reviews'))
        self.assertEqual(response.status_code, 200)
