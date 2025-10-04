"""
Platform-specific authentication modules.

This package includes modules for Windows, macOS, and Linux, each providing
synchronous and asynchronous functions to authenticate users using the
native authentication methods of the respective operating system.
"""

from . import linux, macos, windows

__all__ = ["linux", "macos", "windows"]
