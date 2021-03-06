from rest_framework.views import APIView
from rest_framework.response import Response

from .services import GetNewsService
from .serializers import NewsSerializer


class AllNewsView(APIView):
    """View to return all news"""

    service = GetNewsService()

    def get(self, request):
        """Return all news"""
        all_news = self.service.get_all()
        serialized_news = NewsSerializer(all_news, many=True)
        return Response(serialized_news.data)
