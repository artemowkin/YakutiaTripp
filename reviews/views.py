from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

from utils.views import validation_decorator
from .services import (
    GetReviewsService, CreateReviewService, set_review_avatar
)
from .serializers import ReviewSerializer


class AllReviewsView(APIView):
    """View to return all reviews"""

    get_service = GetReviewsService()
    create_service = CreateReviewService()

    def get(self, request):
        all_reviews = self.get_service.get_all()
        reviews_serializer = ReviewSerializer(all_reviews, many=True)
        return Response(reviews_serializer.data)

    @validation_decorator
    def post(self, request):
        review = self.create_service.create(**request.data)
        review_serializer = ReviewSerializer(review)
        return Response(review_serializer.data, status=201)


class SetReviewAvatarView(APIView):
    """View to set avatar for review"""

    parser_classes = (FileUploadParser,)
    get_service = GetReviewsService()

    def patch(self, request, pk):
        file_obj = request.data['file']
        review = self.get_service.get_concrete(pk)
        set_review_avatar(review, file_obj)
        return Response({'avatar': review.avatar.url})
