"""
Local authentication using system biometric or password authentication.

*Automatically imports the appropriate platform-specific module based on the operating system.*
"""

__version__ = "1.0.0"

import platform

from .exceptions import AuthError, AuthUnavailableError, RequiredLibError

match platform.system():
    case "Windows":
        from .platforms.windows import (
            authenticate,
            authenticate_async,
            is_available,
            is_available_async,
        )
    case "Darwin":
        from .platforms.macos import (
            authenticate,
            authenticate_async,
            is_available,
            is_available_async,
        )
    case "Linux":
        from .platforms.linux import (
            authenticate,
            authenticate_async,
            is_available,
            is_available_async,
        )
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
