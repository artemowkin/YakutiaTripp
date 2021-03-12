from uuid import UUID

from django.db.models import QuerySet

from services.base import BaseGetService
from .models import Tour


class GetToursService(BaseGetService):
    """Service to get tours"""

    model = Tour

    def get_concrete(self, pk: UUID) -> Tour:
        """Return a concrete tour with incremented views"""
        tour = super().get_concrete(pk)
        tour.views = tour.views + 1
        tour.save()
        return tour

    def get_most_viewed(self) -> QuerySet:
        """Return 3 most viewed tours"""
        most_viewed_tours = self.get_all().order_by('-views')[:9]
        return most_viewed_tours
