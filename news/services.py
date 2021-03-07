from django.db.models import QuerySet

from services.base import BaseGetService
from .models import News


class GetNewsService(BaseGetService):
    """Service to get news entries"""

    model = News

    def get_last(self) -> QuerySet:
        """Return last 9 news"""
        return self.model.objects.all()[:9]
