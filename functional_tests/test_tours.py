import datetime

import requests
from django.test import LiveServerTestCase

from tours.models import Tour, TourDay


class ToursEndpointsTest(LiveServerTestCase):
    """Test of tours endpoints"""

    def setUp(self):
        self.current_weekday = self._get_current_weekday()
        self.tour = Tour.objects.create(
            title="new tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        self.tour_day = TourDay.objects.create(
            weekday=self.current_weekday, description="hike", tour=self.tour
        )

    def _get_current_weekday(self):
        """Return today weekday"""
        weekdays = [
            'monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'sunday'
        ]
        today_weekday = datetime.date.today().weekday()
        return weekdays[today_weekday]

    def test_api_tours_endpoint_returns_correct_data(self):
        """Test: does /api/tours/ endpoint returns correct data"""
        response = requests.get(self.live_server_url + '/api/tours/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), Tour.objects.count())
        self.assertEqual(response.json()[0], {
            'pk': str(self.tour.pk), 'title': 'new tour',
            'preview': '/media/hello.png', 'short_description': 'some words',
            'days': [{'weekday': self.current_weekday, 'description': 'hike'}],
            'about': 'some about', 'price': '100.00', 'city_from': 'LA',
            'city_to': 'LA', 'views': 0
        })

    def test_api_tours_for_concrete_tour_endpoint_returns_correct_data(self):
        """Test: does /api/tours/ endpoint returns correct data"""
        response = requests.get(
            self.live_server_url + f'/api/tours/{self.tour.pk}/'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'pk': str(self.tour.pk), 'title': 'new tour',
            'preview': '/media/hello.png', 'short_description': 'some words',
            'days': [{'weekday': self.current_weekday, 'description': 'hike'}],
            'about': 'some about', 'price': '100.00', 'city_from': 'LA',
            'city_to': 'LA', 'views': 1
        })

    def test_api_tours_most_viewed_returns_correct_data(self):
        """Test: does /api/tours/most_viewed/ endpoint return correct data"""
        for i in range(9):
            Tour.objects.create(
                title=f"tour {i}", preview="hello.png",
                short_description="some words", about="some about",
                price="100.00", city_from="LA", city_to="LA"
            )

        self.tour.views = self.tour.views + 1
        self.tour.save()

        response = requests.get(
            self.live_server_url + '/api/tours/most_viewed/'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 9)
        self.assertIn({
            'pk': str(self.tour.pk), 'title': 'new tour',
            'preview': '/media/hello.png', 'short_description': 'some words',
            'days': [{'weekday': self.current_weekday, 'description': 'hike'}],
            'about': 'some about', 'price': '100.00', 'city_from': 'LA',
            'city_to': 'LA', 'views': 1
        }, response.json())

    def test_api_tours_search_returns_correct_data(self):
        """Test: /api/tours/search/ returns correct data"""
        second_tour = Tour.objects.create(
            title=f"second tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="Moscow", city_to="Moscow"
        )
        response = requests.get(
            self.live_server_url +
            f'/api/tours/search/LA/LA/{datetime.date.today()}/',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertIn({
            'pk': str(self.tour.pk), 'title': 'new tour',
            'preview': '/media/hello.png', 'short_description': 'some words',
            'days': [{'weekday': self.current_weekday, 'description': 'hike'}],
            'about': 'some about', 'price': '100.00', 'city_from': 'LA',
            'city_to': 'LA', 'views': 0
        }, response.json())
