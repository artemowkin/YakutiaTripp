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


class ConcreteNewsView(APIView):
    """View to return a concrete news"""

    service = GetNewsService()

    def get(self, request, pk):
        """Return a concrete news"""
        news = self.service.get_concrete(pk)
        serialized_news = NewsSerializer(news)
        return Response(serialized_news.data)


class LastNewsView(APIView):
    """View to return last news"""

    service = GetNewsService()

    def get(self, request):
        """Return last news"""
        news = self.service.get_last()
        serialized_news = NewsSerializer(news, many=True)
        return Response(serialized_news.data)
