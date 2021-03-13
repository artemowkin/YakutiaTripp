import uuid

from django.test import TestCase

from ..models import Tour, TourDay


class TourDayTest(TestCase):
    """Case of testing Tour model"""

    def setUp(self):
        self.tour = Tour.objects.create(
            title="new tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        self.tour_day = TourDay.objects.create(
            weekday="monday", description="hike", tour=self.tour
        )

    def test_create_entry_fields(self):
        """Test: does Tour model create an entry"""
        self.assertEqual(TourDay.objects.count(), 1)
        self.assertEqual(TourDay.objects.first(), self.tour_day)

    def test_create_entry(self):
        self.assertEqual(self.tour_day.weekday, 'monday')
        self.assertEqual(self.tour_day.description, 'hike')
        self.assertEqual(self.tour_day.tour, self.tour)

    def test_string_representation(self):
        """Test: does TourDay entry __str__ returns tour day description"""
        self.assertEqual(str(self.tour_day), self.tour_day.description)


class TourTest(TestCase):
    """Case of testing Tour model"""

    def setUp(self):
        self.tour = Tour.objects.create(
            title="new tour", preview="hello.png",
            short_description="some words", about="some about",
            price="100.00", city_from="LA", city_to="LA"
        )
        self.tour_day = TourDay.objects.create(
            weekday="monday", description="hike", tour=self.tour
        )

    def test_create_entry(self):
        """Test: does Tour model create an entry"""
        self.assertEqual(Tour.objects.count(), 1)
        self.assertEqual(Tour.objects.first(), self.tour)

    def test_created_entry_fields(self):
        """Test: does Tour model create correct entry with correct fields"""
        self.assertEqual(self.tour.title, 'new tour')
        self.assertEqual(self.tour.preview.url, '/media/hello.png')
        self.assertEqual(self.tour.short_description, 'some words')
        self.assertEqual(self.tour.about, 'some about')
        self.assertEqual(self.tour.price, '100.00')
        self.assertEqual(self.tour.city_from, 'LA')
        self.assertEqual(self.tour.city_to, 'LA')

    def test_tour_days_related_field(self):
        """Test: has Tour entry days attribute to work with related days"""
        self.assertTrue(hasattr(self.tour, 'days'))
        self.assertIn(self.tour_day, self.tour.days.all())

    def test_string_representation(self):
        """Test: does Tour model entry __str__ return tour title"""
        self.assertEqual(str(self.tour), self.tour.title)

    def test_pk_is_uuid(self):
        """Test: is model pk UUID field"""
        self.assertIsInstance(self.tour.pk, uuid.UUID)
