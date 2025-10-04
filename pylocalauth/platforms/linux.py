"""
Linux PAM Authentication for Python

Provides synchronous and asynchronous functions to authenticate users
via PAM (Pluggable Authentication Modules). Includes availability checks
and detailed exceptions. Logging is included for debugging purposes.

**NOTE**: This module requires the `python-pam` and `six` packages.
Install them via pip if not already installed:
```python
pip install python-pam six --upgrade
```
"""

import asyncio
import getpass
import logging

from ..exceptions import AuthUnavailableError, RequiredLibError

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__all__ = ["is_available", "is_available_async", "authenticate", "authenticate_async"]

try:
    import pam
except ImportError:
    raise RequiredLibError(
        "Linux authentication requires the `python-pam` and `six` packages "
        "(`pip install python-pam six --upgrade`)."
    )


async def is_available_async() -> bool:
    """
    Asynchronously checks if PAM authentication is available on this device.

    :return: True if available, False otherwise
    """
    logger.debug("Checking Linux PAM authentication availability...")
    # On most Linux systems, PAM is always available if the module is importable
    available = True
    logger.debug(f"Linux PAM authentication available: {available}")
    return available


def is_available() -> bool:
    """
    Synchronously checks if PAM authentication is available on this device.

    :return: True if available, False otherwise
    """
    return asyncio.run(is_available_async())


async def authenticate_async(
    message: str = "Authenticate to continue",
    check_availability: bool = True,
    username: str | None = None,
) -> bool:
    """
    Asynchronously performs Linux PAM authentication.

    :param message: Message to display in the authentication prompt
    :param check_availability: If True, raises AuthError if not available
    :param username: Username to authenticate (defaults to current user)
    :return: True if authentication succeeds, False otherwise
    :raises AuthError: if authentication is not available and check_availability is True
    """
    logger.debug("Starting async Linux PAM authentication...")
    if check_availability:
        available = await is_available_async()
        if not available:
            logger.warning("Linux PAM authentication is not available.")
            raise AuthUnavailableError("Linux PAM authentication is not available.")
        logger.debug("Linux PAM authentication is available.")

    if username is None:
        username = getpass.getuser()

    loop = asyncio.get_running_loop()
    future = loop.create_future()

    def prompt_password():
        try:
            password = getpass.getpass(f"{message} (user: {username}): ")
            p = pam.pam()
            success = p.authenticate(username, password)
            logger.info(
                "Linux PAM authentication succeeded."
                if success
                else "Linux PAM authentication failed."
            )
            loop.call_soon_threadsafe(future.set_result, success)
        except Exception as e:
            logger.error(f"Linux PAM authentication error: {e}")
            loop.call_soon_threadsafe(future.set_result, False)

    await loop.run_in_executor(None, prompt_password)
    return await future


def authenticate(
    message: str = "Authenticate to continue",
    username: str | None = None,
) -> bool:
    """
    Synchronously performs Linux PAM authentication.

    :param message: Message to display in the authentication prompt
    :param username: Username to authenticate (defaults to current user)
    :return: True if authentication succeeds, False otherwise
    :raises AuthError: if authentication is not available
    """
    return asyncio.run(authenticate_async(message, username=username))
