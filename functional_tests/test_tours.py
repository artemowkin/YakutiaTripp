import simplejson as json

from django.test import LiveServerTestCase
from django.urls import reverse

from tours.models import Tour, TourDay


class ToursEndpointsTest(LiveServerTestCase):
    """Test of tours endpoints"""

    def setUp(self):
        self.tour = Tour.objects.create(
            title="new tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        self.tour_day = TourDay.objects.create(
            weekday="Monday", description="hike", tour=self.tour
        )

    def test_api_tours_endpoint_returns_correct_data(self):
        """Test: does /api/tours/ endpoint returns correct data"""
        response = self.client.get(reverse('all_tours'))
        response_json = json.loads(response.content)

        self.assertEqual(len(response_json), Tour.objects.count())
        self.assertEqual(response_json[0], {
            'pk': str(self.tour.pk), 'title': 'new tour',
            'preview': '/media/hello.png', 'short_description': 'some words',
            'days': [{'weekday': 'Monday', 'description': 'hike'}],
            'about': 'some about', 'price': '100.00', 'city_from': 'LA',
            'city_to': 'LA', 'views': 0
        })
