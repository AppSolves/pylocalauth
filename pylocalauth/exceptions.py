"""
Custom exceptions for the `pylocalauth` package.

This module defines exceptions that are used to handle authentication errors
and issues related to platform support and required libraries.
"""


class AuthError(PermissionError):
    """Raised when authentication fails or is not available."""

    pass


class AuthUnavailableError(AuthError):
    """Raised when authentication is not available on the current platform."""

    pass


class RequiredLibError(ImportError):
    """Raised when a required library is not installed."""

    pass
