from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet


class BaseGetService:
    """Base service to get model entries"""

    model = None

    def __init__(self):
        if not self.model:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} must include `model` attribute"
            )

    def get_all(self) -> QuerySet:
        """Return all model entries"""
        return self.model.objects.all()
