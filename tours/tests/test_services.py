from django.test import TestCase

from ..services import GetToursService
from ..models import Tour, TourDay


class GetToursServiceTest(TestCase):
    """Case of testing service to get all tours"""

    def setUp(self):
        self.service = GetToursService()
        self.tour = Tour.objects.create(
            title="new tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        self.tour_day = TourDay.objects.create(
            weekday="Monday", description="hike", tour=self.tour
        )

    def test_get_all_returns_all_entries(self):
        """Test: get_all method returns all tours"""
        all_tours = self.service.get_all()

        self.assertEqual(all_tours.count(), Tour.objects.count())
        self.assertEqual(all_tours[0], self.tour)
