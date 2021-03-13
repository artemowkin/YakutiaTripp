from django.test import TestCase

from ..services import GetToursService, SearchToursService
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
            weekday="monday", description="hike", tour=self.tour
        )

    def test_get_all_returns_all_entries(self):
        """Test: get_all method returns all tours"""
        all_tours = self.service.get_all()

        self.assertEqual(all_tours.count(), Tour.objects.count())
        self.assertEqual(all_tours[0], self.tour)

    def test_get_concrete_returns_correct_tour_with_incremented_views(self):
        """Test: get_concrete returns a concrete tour with 1 views"""
        tour = self.service.get_concrete(self.tour.pk)

        self.assertEqual(tour, self.tour)
        self.assertEqual(tour.views, 1)

    def test_get_most_viewed_returns_three_most_viewed_tours(self):
        """Test: get_most_viewed returns 3 most viewed tours"""
        for i in range(9):
            Tour.objects.create(
                title=f"tour {i}", preview="hello.png",
                short_description="some words", about="some about",
                price="100.00", city_from="LA", city_to="LA"
            )

        self.tour.views = self.tour.views + 1
        self.tour.save()

        tours = self.service.get_most_viewed()

        self.assertEqual(tours.count(), 9)
        self.assertEqual(tours[0], self.tour)


class SearchToursServiceTest(TestCase):
    """Case of testing service to search tours"""

    def setUp(self):
        self.service = SearchToursService()
        self.tour = Tour.objects.create(
            title="new tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        self.tour_day = TourDay.objects.create(
            weekday="monday", description="hike", tour=self.tour
        )

    def test_search_returns_correct_tours(self):
        """Test: does search method returns correct tours"""
        second_tour = Tour.objects.create(
            title=f"second tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        second_tour_day = TourDay.objects.create(
            weekday="sunday", description="hike", tour=second_tour
        )

        tours = self.service.search(
            city_from="LA", city_to="LA", date="2021-03-15"
        )
        self.assertIn(self.tour, tours)
