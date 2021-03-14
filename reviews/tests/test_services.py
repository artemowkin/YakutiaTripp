from django.test import TestCase

from ..services import GetReviewsService
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
        not_moderated_review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
        )
        all_reviews = self.service.get_all()
        self.assertEqual(len(all_reviews), 1)
        self.assertEqual(all_reviews[0], self.review)
