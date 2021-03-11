from django.test import TestCase

from ..models import Tour, TourDay
from ..serializers import TourSerializer


class TourSerializerTest(TestCase):
    """Case of testing TourSerializer"""

    def test_correct_serializing_tour_model_entry(self):
        tour = Tour.objects.create(
            title="new tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        tour_day = TourDay.objects.create(
            weekday="Monday", description="hike", tour=tour
        )
        serializer = TourSerializer(tour)
        serialized_tour = dict(serializer.data)
        serialized_tour['days'] = [
            dict(day) for day in serialized_tour['days']
        ]

        self.assertEqual(serialized_tour, {
            'pk': str(tour.pk), 'title': 'new tour',
            'preview': '/media/hello.png', 'short_description': 'some words',
            'days': [{'weekday': 'Monday', 'description': 'hike'}],
            'about': 'some about', 'price': '100.00', 'city_from': 'LA',
            'city_to': 'LA', 'views': 0
        })
