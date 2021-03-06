from uuid import UUID

from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet, Model
from django.shortcuts import get_object_or_404


class BaseService:
    """Base service class"""

    model = None

    def __init__(self):
        if not self.model:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} must include `model` attribute"
            )


class BaseGetService(BaseService):
    """Base service to get model entries"""

    def get_all(self) -> QuerySet:
        """Return all model entries"""
        return self.model.objects.all()

    def get_concrete(self, pk: UUID) -> Model:
        """Return a concrete model entry by pk"""
        return get_object_or_404(self.model, pk=pk)
