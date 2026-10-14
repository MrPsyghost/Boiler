from loc import TEMPLATES_DIR
from tqdm.auto import tqdm
from shutil import rmtree


def _templates_():
    if TEMPLATES_DIR.exists():
        return [f.name for f in TEMPLATES_DIR.iterdir() if f.is_dir()]
    TEMPLATES_DIR.mkdir(exist_ok=True)
    return []


def _remove_all_templates_():
    if TEMPLATES_DIR.exists():
        if len(list(TEMPLATES_DIR.iterdir())) == 0:
            print('error: nothing to remove.')
            return
        (TEMPLATES_DIR / 'current_template.cfg').unlink(missing_ok=True)
        ufs = []
        for f in tqdm(list(TEMPLATES_DIR.iterdir()), desc='deleting templates'):
            if f.is_dir():
                rmtree(f)
            if f.is_file():
                ufs.append(f.name)
        for i in ufs:
            print(f"a file named '{i}' was found in the templates directory.")
    TEMPLATES_DIR.mkdir(exist_ok=True)
    print('successfully removed all templates.')


def _remove_template_(name: str):
    if TEMPLATES_DIR.exists():
        template = (TEMPLATES_DIR / name)
        if template.exists():
            template.rmdir()
            (TEMPLATES_DIR / 'current_template.cfg').unlink(missing_ok=True)
            return True
    TEMPLATES_DIR.mkdir(exist_ok=True)
    return False


def _create_template_(name: str):
    if name not in _templates_():
        (TEMPLATES_DIR / name).mkdir()
        return True
    return False