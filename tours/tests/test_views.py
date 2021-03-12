from django.test import TestCase
from django.urls import reverse

from ..models import Tour


class AllToursViewTest(TestCase):
    """Case of testing AllToursView"""

    def test_response_status_code(self):
        """Test: is view response has correct status code"""
        response = self.client.get(reverse('all_tours'))
        self.assertEqual(response.status_code, 200)


class ConcreteTourViewTest(TestCase):
    """Case of testing ConcreteTourView"""

    def test_response_status_code(self):
        """Test: is view response has correct status code"""
        self.tour = Tour.objects.create(
            title="new tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        response = self.client.get(
            reverse('concrete_tour', args=[self.tour.pk])
        )
        self.assertEqual(response.status_code, 200)
