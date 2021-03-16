from django.db.models import QuerySet

from services.base import BaseGetService, BaseService
from .models import Review


class GetReviewsService(BaseGetService):
    """Service to get reviews"""

    model = Review

    def get_all(self) -> QuerySet:
        """Return all moderated reviews"""
        all_reviews = super().get_all()
        return all_reviews.filter(moderated=True)


class CreateReviewService(BaseService):
    """Service to create a new review"""

    model = Review

    def create(self, name: str, rating: int, text: str) -> Review:
        """Create a new review using name, rating, and text"""
        created_review = self.model.objects.create(
            name=name, rating=rating, text=text
        )
        created_review.full_clean()
        return created_review


def set_review_avatar(review, file_obj):
    """Set avatar for review"""
    review.avatar = file_obj
    review.save()
