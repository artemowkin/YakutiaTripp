import os
from typing import Union, Any

from django.core.exceptions import ImproperlyConfigured


def get_env(env_name: str, default: Any = "") -> Union[str, int]:
    """Return environment variable. Raise ImproperlyConfigured if
    variable doesn't exist
    """
    env_variable = os.getenv(env_name, default)
    _check_env_variable(env_name, env_variable)
    env_variable = _format_env_variable(env_variable)
    return env_variable


def _check_env_variable(env_name: str, env_var: Any) -> None:
    """Check is environment variable valid"""
    if isinstance(env_var, str) and not env_var:
        raise ImproperlyConfigured(
            f"You need to set {env_name} environment variable"
        )


def _format_env_variable(env_var: Any) -> Any:
    """Format environment variable to integer if it includes
    only numbers
    """
    if isinstance(env_var, str) and env_var.isnumeric():
        return int(env_var)

    return env_var
