from rest_framework.views import APIView
from rest_framework.response import Response

from .services import GetReviewsService, CreateReviewService
from .serializers import ReviewSerializer


class AllReviewsView(APIView):
    """View to return all reviews"""

    get_service = GetReviewsService()
    create_service = CreateReviewService()

    def get(self, request):
        all_reviews = self.get_service.get_all()
        reviews_serializer = ReviewSerializer(all_reviews, many=True)
        return Response(reviews_serializer.data)

    def post(self, request):
        review = self.create_service.create(**request.data)
        review_serializer = ReviewSerializer(review)
        return Response(review_serializer.data, status=201)
