import re
import os
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

    def test_api_reviews_POST_with_incorrect_rating_returns_error(self):
        """Test: does POST /api/reviews/ with incorrect rating returns
        400 Bad Request and error message"""
        response = requests.post(self.live_server_url + '/api/reviews/', json={
            'name': 'Username', 'rating': 6, 'text': 'some text'
        })

        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.json()['rating'])

    def test_api_review_set_avatar(self):
        """Test: does PATCH /api/reviews/{review_pk}/ change review avatar"""
        with open(settings.BASE_DIR / 'static/img/avatar1.jpg', 'rb') as fb:
            files = {'avatar.jpg': fb}
            response = requests.patch(
                self.live_server_url + f'/api/reviews/{self.review.pk}/',
                files=files, headers={
                    'Content-Disposition': 'attachment; filename="avatar.jpg"'
                }
            )

        self.assertEqual(response.status_code, 200)
        self.assertRegex(
            response.json()['avatar'], r'/media/reviews/avatar.*\.jpg'
        )

        os.remove(settings.BASE_DIR / response.json()['avatar'][1:])
