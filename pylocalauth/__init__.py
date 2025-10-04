"""
Local authentication using system biometric or password authentication.
"""

__version__ = "1.0.0"

import platform

from .exceptions import AuthError, AuthUnavailableError, RequiredLibError

match platform.system():
    case "Windows":
        from .platforms.windows import *
    case "Darwin":
        from .platforms.macos import *
    case "Linux":
        from .platforms.linux import *
    case _:
        raise ImportError(f"Unsupported platform: {platform.system()}")

__all__ = [
    "is_available",
    "is_available_async",
    "authenticate",
    "authenticate_async",
    "AuthError",
    "AuthUnavailableError",
    "RequiredLibError",
]
