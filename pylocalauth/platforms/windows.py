"""
**Windows Hello Authentication for Python**

Provides synchronous and asynchronous functions to authenticate users
via *Windows Hello* (biometrics or PIN). Includes availability checks
and detailed exceptions. Logging is included for debugging purposes.

**NOTE**: This module requires the `winrt-Windows.Security.Credentials.UI` package.
Install it via pip if not already installed:
```python
pip install winrt-Windows.Security.Credentials.UI --upgrade
```

**This API requires `Windows 10` or later.**
"""

import asyncio
import logging

from ..exceptions import AuthUnavailableError, RequiredLibError

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__all__ = ["is_available", "is_available_async", "authenticate", "authenticate_async"]

try:
    from winrt.windows.security.credentials.ui import (
        UserConsentVerificationResult as VerificationResult,
    )
    from winrt.windows.security.credentials.ui import UserConsentVerifier as _Verifier
except ImportError:
    raise RequiredLibError(
        "Windows authentication requires `winrt` package "
        "(`pip install winrt-Windows.Security.Credentials.UI --upgrade`)."
    )


async def is_available_async() -> bool:
    """
    Asynchronously checks if Windows Hello is available on this device.

    :return: True if Windows Hello is available, False otherwise
    """
    logger.debug("Checking Windows Hello availability...")
    availability = await _Verifier.check_availability_async()
    is_available = availability == 0  # 0 == Available
    logger.debug(f"Windows Hello available: {is_available}")
    return is_available


def is_available() -> bool:
    """
    Synchronously checks if Windows Hello is available on this device using `asyncio.run`.

    :return: True if Windows Hello is available, False otherwise
    """
    return asyncio.run(is_available_async())


async def authenticate_async(
    message: str = "Authenticate to continue",
    check_availability: bool = True,
) -> bool:
    """
    Asynchronously performs Windows Hello authentication.

    :param message: Message to display in the Windows Hello prompt
    :param check_availability: If True, raises AuthError if Hello is not available
    :return: True if authentication succeeds, False otherwise
    :raises AuthError: if Windows Hello is not available and check_availability is True
    """
    logger.debug("Starting async Windows Hello authentication...")
    if check_availability:
        available = await is_available_async()
        if not available:
            logger.warning("Windows Hello authentication is not available.")
            raise AuthUnavailableError("Windows authentication is not available.")
        logger.debug("Windows Hello is available.")

    result = await _Verifier.request_verification_async(message)
    success = result == VerificationResult.VERIFIED
    if success:
        logger.info("Windows Hello authentication succeeded.")
    else:
        logger.warning("Windows Hello authentication failed.")
    return success


def authenticate(message: str = "Authenticate to continue") -> bool:
    """
    Synchronously performs Windows Hello authentication using `asyncio.run`.

    :param message: Message to display in the Windows Hello prompt
    :return: True if authentication succeeds, False otherwise
    :raises AuthError: if Windows Hello is not available
    """
    return asyncio.run(authenticate_async(message))
