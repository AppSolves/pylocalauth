# flake8: noqa
import sys

try:
    from pylocalauth import __version__
except Exception as e:
    print(f"Import failed: {e}")
    sys.exit(1)

print(f"`pylocalauth` version: {__version__}")
sys.exit(0)
