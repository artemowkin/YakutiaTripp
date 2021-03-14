import datetime

import requests
from django.test import LiveServerTestCase

from reviews.models import Review


class ReviewsEndpointsTest(LiveServerTestCase):
    """Test of reviews endpoints"""

    def setUp(self):
        self.review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
            moderated=True
        )

    def test_api_reviews_returns_correct_data(self):
        """Test: does /api/reviews/ endpoints returns correct date"""
        not_moderated_review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
        )
        response = requests.get(self.live_server_url + '/api/reviews/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertIn({
            'pk': str(self.review.pk), 'name': 'Some review',
            'avatar': '/media/reviews/default_review_avatar.jpg',
            'rating': 5, 'text': 'some review text', 'moderated': True,
            'pub_date': datetime.date.today().isoformat()
        }, response.json())
