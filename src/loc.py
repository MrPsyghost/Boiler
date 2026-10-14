import sys
from pathlib import Path


if getattr(sys, "frozen", False):
    BOILER_DIR = Path(sys.executable).parent
    TEMPLATES_DIR = BOILER_DIR / '_internal' / 'templates'
else:
    BOILER_DIR = Path(__file__).parent
    TEMPLATES_DIR = BOILER_DIR / 'templates'
