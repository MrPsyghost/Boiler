import argparse, sys, pyfiglet
from actions import actions
from config import _config_
from templates import _templates_
from termcolor import cprint
import boil, remove, add, clear, set, list_templates, path_templates, init, donate


parser = argparse.ArgumentParser(
    prog='Boiler',
    description='Boiler',
    epilog='Thanks for using Boiler.',
)

parser.add_argument('-v', '--version', action='store_true', help='shows the installed version of boiler and the latest update version')
parser.add_argument('action', nargs='?', help='boil/init/set/add/clear/list/remove/path')
parser.add_argument("paths", nargs="*", help="files or directories to add")
parser.add_argument('-n', '--name', help=f"name of the template (if not provided, name is set to 'template{len(_templates_())}')")
parser.add_argument('-a', '--all', action='store_true', help='removes all the existing templates.')
# parser.add_argument('-cu', '--currency', help='set another currency (default is INR).')

args = parser.parse_args()

if args.version:
    cfg = _config_()
    if 'error' in list(cfg.keys()):
        print('error:', cfg['error'])
    else:
        if cfg['showBanner'] == 'true':
            cprint(pyfiglet.figlet_format(cfg['name'], font=cfg['asciiFont']), cfg['color'].lower(), end='')
        cprint(f"v{cfg['version']} ({cfg['versionType']})", cfg['color'].lower())
        cprint(cfg['author'], 'red', attrs=['bold'])
        cprint(cfg['description'], 'black')
        cprint(f"{cfg['license']} License", 'light_blue', attrs=['bold'])
    sys.exit(0)


if args.action:
    try:
        actions[args.action](args)
    except KeyError:
        print(f"error: unknown action '{args.action}'.")
else:
    print('error: action not provided.')
    sys.exit(1)