"""
**macOS Local Authentication for Python**

Provides synchronous and asynchronous functions to authenticate users
via *Touch ID or password*. Includes availability checks and detailed exceptions.
Logging is included for debugging purposes.

**NOTE**: This module requires the `pyobjc` and `pyobjc-framework-LocalAuthentication`
packages. Install them via pip if not already installed:
```python
pip install pyobjc pyobjc-framework-LocalAuthentication --upgrade
```

**This API requires `macOS 10.12` or later.**
"""

import asyncio
import logging
from typing import Any

from ..exceptions import AuthUnavailableError, RequiredLibError

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__all__ = ["is_available", "is_available_async", "authenticate", "authenticate_async"]

try:
    import objc
    from LocalAuthentication import (
        LAContext,
        LAPolicyDeviceOwnerAuthentication,
        LAPolicyDeviceOwnerAuthenticationWithBiometrics,
    )
except ImportError:
    raise RequiredLibError(
        "macOS authentication requires the `pyobjc` and `pyobjc-framework-LocalAuthentication` "
        "packages (`pip install pyobjc pyobjc-framework-LocalAuthentication --upgrade`)."
    )


async def is_available_async() -> bool:
    """
    Asynchronously checks if biometric authentication is available on this device.

    :return: True if available, False otherwise
    """
    logger.debug("Checking macOS biometric authentication availability...")
    context = LAContext.alloc().init()
    error = objc.nil
    available = context.canEvaluatePolicy_error_(
        LAPolicyDeviceOwnerAuthenticationWithBiometrics, error
    )
    logger.debug(f"macOS biometric authentication available: {bool(available)}")
    return bool(available)


def is_available() -> bool:
    """
    Synchronously checks if biometric authentication is available on this device.

    :return: True if available, False otherwise
    """
    return asyncio.run(is_available_async())


async def authenticate_async(
    message: str = "Authenticate to continue",
    check_availability: bool = True,
) -> bool:
    """
    Asynchronously performs macOS authentication.

    :param message: Message to display in the authentication prompt
    :param check_availability: If True, raises AuthError if not available
    :return: True if authentication succeeds, False otherwise
    :raises AuthError: if authentication is not available and check_availability is True
    """
    logger.debug("Starting async macOS authentication...")
    context = LAContext.alloc().init()
    error = objc.nil

    if check_availability:
        available = context.canEvaluatePolicy_error_(
            LAPolicyDeviceOwnerAuthentication, error
        )
        if not available:
            logger.warning("macOS authentication is not available.")
            raise AuthUnavailableError("macOS authentication is not available.")
        logger.debug("macOS authentication is available.")

    loop = asyncio.get_running_loop()
    future = loop.create_future()

    def reply(success: bool, error_obj: Any) -> None:
        if success:
            logger.info("macOS authentication succeeded.")
            loop.call_soon_threadsafe(future.set_result, True)
        else:
            if error_obj:
                logger.debug(f"macOS auth error object: {error_obj}")
            logger.warning("macOS authentication failed.")
            loop.call_soon_threadsafe(future.set_result, False)

    context.evaluatePolicy_localizedReason_reply_(
        LAPolicyDeviceOwnerAuthentication,
        message,
        reply,
    )

    return await future


def authenticate(message: str = "Authenticate to continue") -> bool:
    """
    Synchronously performs macOS authentication.

    :param message: Message to display in the authentication prompt
    :return: True if authentication succeeds, False otherwise
    :raises AuthError: if authentication is not available
    """
    return asyncio.run(authenticate_async(message))
