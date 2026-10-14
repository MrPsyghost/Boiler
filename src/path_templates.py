from loc import TEMPLATES_DIR
from actions import register


@register("path")
def path_templates(args):
    if args.name:
        if (TEMPLATES_DIR / args.name).exists():
            print(TEMPLATES_DIR / args.name)
        else:
            print(f"error: no template found with the name '{args.name}'.")
    else:
        print(TEMPLATES_DIR)