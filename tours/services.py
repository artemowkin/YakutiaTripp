import datetime
from uuid import UUID

from django.db.models import QuerySet

from services.base import BaseGetService, BaseService
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


class SearchToursService(BaseService):
    """Service to search tours"""

    model = Tour

    def search(self, city_from: str, city_to: str, date: str) -> QuerySet:
        """Search tours with city_from, city_to, and date weekday"""
        date_weekday = self._get_weekday(date)
        return self.model.objects.filter(
            city_from=city_from, city_to=city_to, days__weekday=date_weekday
        )

    def _get_weekday(self, date: str) -> int:
        """Return weekday of date"""
        weekdays = [
            'monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'sunday'
        ]
        date = datetime.date.fromisoformat(date)
        date_weekday_number = date.weekday()
        return weekdays[date_weekday_number]
