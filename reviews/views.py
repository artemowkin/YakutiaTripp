from rest_framework.views import APIView
from rest_framework.response import Response

from .services import GetReviewsService
from .serializers import ReviewSerializer


class AllReviewsView(APIView):
    """View to return all reviews"""

    service = GetReviewsService()

    def get(self, request):
        all_reviews = self.service.get_all()
        reviews_serializer = ReviewSerializer(all_reviews, many=True)
        return Response(reviews_serializer.data)
