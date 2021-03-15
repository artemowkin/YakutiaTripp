from django.test import TestCase

from ..services import GetReviewsService, CreateReviewService
from ..models import Review


class GetReviewsServiceTest(TestCase):
    """Case of testing service to get all reviews"""

    def setUp(self):
        self.service = GetReviewsService()
        self.review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
            moderated=True
        )

    def test_get_all_returns_all_moderated_reviews(self):
        """Test: get_all method returns all moderated reviews"""
        not_moderated_review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
        )
        all_reviews = self.service.get_all()
        self.assertEqual(len(all_reviews), 1)
        self.assertEqual(all_reviews[0], self.review)


class CreateReviewServiceTest(TestCase):
    """Case of testing service to create a new review"""

    def setUp(self):
        self.service = CreateReviewService()

    def test_create_returns_created_review(self):
        """Test: create method returns created review"""
        review_data = {'name': 'Username', 'rating': 5, 'text': 'some text'}
        created_review = self.service.create(**review_data)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.first(), created_review)
