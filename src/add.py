from loc import TEMPLATES_DIR
from actions import register
from pathlib import Path
from shutil import copytree, copy2


@register("add")
def add(args):
    if not args.paths:
        return
    
    excluded_items = []

    if (Path.cwd() / '.boilerignore').exists():
        excluded_items = (Path.cwd() / '.boilerignore').read_text(encoding="utf-8").splitlines()

    with (TEMPLATES_DIR / 'current_template.cfg').open("r", encoding="utf-8") as f:
        DESTINATION = TEMPLATES_DIR / f.read()
    
    for p in args.paths:
        if p == '.':
            for i in list(Path.cwd().iterdir()):
                if i.name != '.boilerignore':
                    if i.name not in excluded_items:
                        if i.is_dir():
                            copytree(i, (DESTINATION / i.name), dirs_exist_ok=True)
                        else:
                            copy2(i, (DESTINATION / i.name))
            continue
        if p not in excluded_items:
            if Path(p).is_dir():
                copytree(Path(p), (DESTINATION / Path(p).name), dirs_exist_ok=True)
            else:
                copy2(Path(p), DESTINATION)