# flake8: noqa
import sys

try:
    from pylocalauth import __version__
except:
    sys.exit(1)

sys.exit(0)
