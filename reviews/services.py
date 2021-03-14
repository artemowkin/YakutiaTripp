from django.db.models import QuerySet

from services.base import BaseGetService
from .models import Review


class GetReviewsService(BaseGetService):
    """Service to get reviews"""

    model = Review

    def get_all(self) -> QuerySet:
        """Return all moderated reviews"""
        all_reviews = super().get_all()
        return all_reviews.filter(moderated=True)
