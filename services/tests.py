from django.test import TestCase
from django.core.exceptions import ImproperlyConfigured

from .base import BaseGetService


class IncorrectService(BaseGetService):
    """Incorrect service without model attribute"""
    pass


class BaseGetServiceTest(TestCase):
    """Case of testing BaseGetService"""

    def test_raise_exception_if_service_has_no_model_attribute(self):
        """Test: does service raise exception when has no model attribute"""
        with self.assertRaises(ImproperlyConfigured):
            IncorrectService()
