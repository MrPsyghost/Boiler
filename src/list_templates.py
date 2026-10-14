from loc import TEMPLATES_DIR
from actions import register


@register("list")
def list_templates(args):
    if TEMPLATES_DIR.exists():
        for i, j in enumerate(list(TEMPLATES_DIR.iterdir())):
            if j.is_dir():
                print(f'{i}. {j.name}')
        return
    TEMPLATES_DIR.mkdir(exist_ok=True)