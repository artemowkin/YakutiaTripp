from services.base import BaseGetService
from .models import Tour


class GetToursService(BaseGetService):
    """Service to get tours"""

    model = Tour
