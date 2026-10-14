from loc import TEMPLATES_DIR
from actions import register
from shutil import rmtree


@register("clear")
def clear(args):
    template = (TEMPLATES_DIR / 'current_template.cfg').open("r", encoding="utf-8").read() if not args.name else args.name
    if (TEMPLATES_DIR / template).exists():
        for i in list((TEMPLATES_DIR / template).iterdir()):
            if i.is_dir():
                rmtree(i)
            if i.is_file():
                i.unlink()