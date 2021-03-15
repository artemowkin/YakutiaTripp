import datetime

import requests
from django.test import LiveServerTestCase
from django.conf import settings

from reviews.models import Review


class ReviewsEndpointsTest(LiveServerTestCase):
    """Test of reviews endpoints"""

    def setUp(self):
        self.review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
            moderated=True
        )

    def test_api_reviews_GET_returns_correct_data(self):
        """Test: does GET /api/reviews/ endpoints returns correct date"""
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

    def test_api_reviews_POST_returns_correct_data(self):
        """Test: does POST /api/reviews/ endpoint returns correct date"""
        response = requests.post(self.live_server_url + '/api/reviews/', json={
            'name': 'Username', 'rating': 5, 'text': 'some text'
        })
        self.assertEqual(response.status_code, 201)
        json_data = response.json()

        self.assertTrue(bool(json_data['pk']))
        self.assertEqual(json_data['name'], 'Username')
        self.assertEqual(
            json_data['avatar'], '/media/reviews/default_review_avatar.jpg'
        )
        self.assertEqual(json_data['rating'], 5)
        self.assertEqual(json_data['text'], 'some text')
        self.assertEqual(json_data['moderated'], False)
        self.assertEqual(
            json_data['pub_date'], datetime.date.today().isoformat()
        )
