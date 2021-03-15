from django.test import TestCase
from django.urls import reverse


class AllReviewsViewTest(TestCase):
    """Case of testing AllReviewsView"""

    def test_GET_response_status_code(self):
        """Test: is view GET response has correct status code"""
        response = self.client.get(reverse('all_reviews'))
        self.assertEqual(response.status_code, 200)

    def test_POST_response_status_code(self):
        """Test: is view POST response has correct status code"""
        response = self.client.post(reverse('all_reviews'), {
            'name': 'Username', 'rating': 5, 'text': 'some text'
        }, content_type='application/json')
        self.assertEqual(response.status_code, 201)
