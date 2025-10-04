"""
Platform-specific authentication modules.

This package includes modules for Windows, macOS, and Linux, each providing
synchronous and asynchronous functions to authenticate users using the
native authentication methods of the respective operating system.
"""

import importlib

from ..exceptions import RequiredLibError

__all__ = ["linux", "macos", "windows"]  # type: ignore
__failed_imports__ = []

for modname in list(__all__):
    try:
        module = importlib.import_module(f".{modname}", __package__)
        globals()[modname] = module
    except (ImportError, RequiredLibError):
        __all__.remove(modname)  # type: ignore
        __failed_imports__.append(modname)
