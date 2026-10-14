from loc import TEMPLATES_DIR
from actions import register
from templates import _templates_, _create_template_


@register("boil")
def boil(args):
    if args.name:
        name = args.name
        if not _create_template_(name):
            print(f'error: a template already exists with the name {args.name}.')
            return
    else:
        name = f'template{len(_templates_())}'
        _create_template_(name)

    with open(TEMPLATES_DIR / 'current_template.cfg', 'w') as f:
        f.write(str(name))
