import uuid
import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Review


class ReviewTest(TestCase):
    """Case of testing Review model"""

    def setUp(self):
        self.review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
            moderated=True
        )

    def test_create_entry(self):
        """Test: does Review model create an entry"""
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.first(), self.review)

    def test_create_entry_fields(self):
        """Test: are created review fields correct"""
        self.assertEqual(self.review.name, 'Some review')
        self.assertEqual(
            self.review.avatar.url, '/media/reviews/default_review_avatar.jpg'
        )
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.text, 'some review text')
        self.assertEqual(self.review.moderated, True)
        self.assertEqual(self.review.pub_date, datetime.date.today())

    def test_string_representation(self):
        """Test: does Review model entry __str__ return review name"""
        self.assertEqual(str(self.review), self.review.name)

    def test_pk_is_uuid(self):
        """Test: is model pk UUID field"""
        self.assertIsInstance(self.review.pk, uuid.UUID)

    def test_rating_max_value(self):
        """Test: rating value greater then 5 is raising ValidationError"""
        incorrect_review = Review.objects.create(
            name="Some review", rating=6, text="some review text",
            moderated=True
        )
        with self.assertRaises(ValidationError):
            incorrect_review.full_clean()

    def test_rating_min_value(self):
        """Test: rating value less then 1 is raising ValidationError"""
        incorrect_review = Review.objects.create(
            name="Some review", rating=0, text="some review text",
            moderated=True
        )
        with self.assertRaises(ValidationError):
            incorrect_review.full_clean()

    def test_ordering(self):
        """Test: are reviews ordering correct"""
        moderated_review_with_low_rating = Review.objects.create(
            name="Some review", rating=2, text="some review text",
            moderated=True
        )
        not_moderated_review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
            moderated=False
        )

        self.assertEqual(list(Review.objects.all()), [
            self.review, moderated_review_with_low_rating, not_moderated_review
        ])
