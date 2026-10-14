from pathlib import Path
from loc import BOILER_DIR


def _config_():
    global BOILER_DIR
    if Path(BOILER_DIR / 'boiler.cfg').exists():
        cfg = {}

        with Path(BOILER_DIR / 'boiler.cfg').open() as f:
            for line in f:
                if not line or '=' not in line:
                    continue
                key, value = line.split('=', 1)
                cfg[key] = value.replace('\n', '')
        
        return cfg
    
    return {'error': 'configuration file not found.'}