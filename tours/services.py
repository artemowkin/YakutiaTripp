from uuid import UUID

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
