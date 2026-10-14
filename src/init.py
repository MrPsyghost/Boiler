from loc import TEMPLATES_DIR
from actions import register
from pathlib import Path
from shutil import copytree


@register("init")
def init(args):
    if not args.paths:
        print('error: no template names were provided to initiate.')
        return

    for i in args.paths:
        if not ((TEMPLATES_DIR / i).exists() and (TEMPLATES_DIR / i).is_dir()):
            print(f"error: no template found with the name '{i}'")
            return
        copytree(TEMPLATES_DIR / i, Path.cwd(), dirs_exist_ok=True)