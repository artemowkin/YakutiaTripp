import datetime

from django.test import TestCase

from ..serializers import ReviewSerializer
from ..models import Review


class ReviewSerializerTest(TestCase):
    """Case of testing ReviewSerializer"""

    def test_correct_serializing_review_model_entry(self):
        """Test: can serializer serialize a Review model entry"""
        review = Review.objects.create(
            name="Some review", rating=5, text="some review text",
            moderated=True
        )
        serializer = ReviewSerializer(review)

        self.assertEqual(serializer.data, {
            'pk': str(review.pk), 'name': 'Some review',
            'avatar': '/media/reviews/default_review_avatar.jpg',
            'rating': 5, 'text': 'some review text', 'moderated': True,
            'pub_date': datetime.date.today().isoformat()
        })
