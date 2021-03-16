from django.core.exceptions import ValidationError
from rest_framework.response import Response


def validation_decorator(view):
    """Decorator with ValidationError handling"""

    def wrapper(*args, **kwargs):
        try:
            return view(*args, **kwargs)
        except ValidationError as e:
            return Response(e.message_dict, status=400)

    return wrapper
