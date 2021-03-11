from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TourSerializer
from .services import GetToursService


class AllToursView(APIView):
    """View to return all tours"""

    service = GetToursService()

    def get(self, request):
        all_tours = self.service.get_all()
        serialized_tours = TourSerializer(all_tours, many=True)
        return Response(serialized_tours.data)
