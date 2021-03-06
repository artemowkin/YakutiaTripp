from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TourSerializer
from .services import GetToursService, SearchToursService


class AllToursView(APIView):
    """View to return all tours"""

    service = GetToursService()

    def get(self, request):
        all_tours = self.service.get_all()
        serialized_tours = TourSerializer(all_tours, many=True)
        return Response(serialized_tours.data)


class ConcreteTourView(APIView):
    """View to return a concrete tour"""

    service = GetToursService()

    def get(self, request, pk):
        tour = self.service.get_concrete(pk)
        serialized_tour = TourSerializer(tour)
        return Response(serialized_tour.data)


class MostViewedToursView(APIView):
    """View to return 3 most viewed tours"""

    service = GetToursService()

    def get(self, request):
        most_viewed_tours = self.service.get_most_viewed()
        serialized_tours = TourSerializer(most_viewed_tours, many=True)
        return Response(serialized_tours.data)


class SearchToursView(APIView):
    """View to search tours by from, to and date"""

    service = SearchToursService()

    def get(self, request, city_from, city_to, date):
        searched_tours = self.service.search(city_from, city_to, date)
        serialized_tours = TourSerializer(searched_tours, many=True)
        return Response(serialized_tours.data)
