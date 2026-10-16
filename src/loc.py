
import sys
import os
from pathlib import Path

if getattr(sys, "frozen", False):
    BOILER_DIR = Path(sys.executable).parent
    DATA_DIR = Path(os.environ["LOCALAPPDATA"]) / "Boiler"
else:
    BOILER_DIR = Path(__file__).resolve().parent
    DATA_DIR = BOILER_DIR

TEMPLATES_DIR = DATA_DIR / "templates"

BOILER_CONFIG = BOILER_DIR / "boiler.cfg"

TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
