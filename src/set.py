from loc import TEMPLATES_DIR
from actions import register


@register("set")
def set(args):
    if args.name:
        if (TEMPLATES_DIR / str(args.name)).exists():
            (TEMPLATES_DIR / 'current_template.cfg').open('w').write(str(args.name))
        else:
            print(f"error: no template exists with the name '{args.name}'.")
    else:
        print('error: no template name provided.')