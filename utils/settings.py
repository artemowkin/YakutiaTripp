import os
from typing import Union, Any

from django.core.exceptions import ImproperlyConfigured


def get_env(env_name: str, default: Any = "") -> Union[str, int]:
    """Return environment variable. Raise ImproperlyConfigured if
    variable doesn't exist
    """
    env_variable = os.getenv(env_name, default)
    if isinstance(env_variable, str) and not env_variable:
        raise ImproperlyConfigured(
            f"You need to set {env_name} environment variable"
        )

    if isinstance(env_variable, str) and env_variable.isnumeric():
        return int(env_variable)

    return env_variable
