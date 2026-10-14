from actions import register
from templates import _remove_all_templates_, _remove_template_


@register("remove")
def remove(args):
    if args.all:
        print('are you sure? (y/n)')
        if input('> ').lower() == 'y':
            _remove_all_templates_()
        else:
            print('aborted.')
    elif args.name:
        print('are you sure? (y/n)')
        if input('> ').lower() == 'y':
            if not _remove_template_(args.name):
                print(f"error: no template with the name '{args.name}' exists.")
        else:
            print('aborted.')
    else:
        print('error: nothing provided to remove.')
