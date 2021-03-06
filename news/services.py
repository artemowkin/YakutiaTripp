from services.base import BaseGetService

from .models import News


class GetNewsService(BaseGetService):
    """Service to get news entries"""

    model = News
