"""
Useful functions/variables for the Toolbox App
"""


import os
import shutil
from datetime import date
from templates.py_templates import MANIFEST_TEMPLATE
from templates.html_templates import INDEX_TEMPLATE


HUROOS_ICON_PATH: str = "assets/huroos_logo.png"


def create_odoo_module(technical_name: str, module_name: str, path: str, module_description: str = "", module_category: str = "Tools", powered_by: str = "Great developer") -> None:
    """Creates a Odoo module in the given path"""

    module_full_path: str = "%s/%s" % (path, technical_name)

    if os.path.exists(module_full_path):
        raise FileExistsError("Il modulo \"%s\" esiste già nel percorso \"%s\"" % (technical_name, path))

    # Module init
    os.makedirs(f"%s/static/description" % module_full_path, exist_ok=True)

    # Manifest
    today = date.today()
    manifest_path: str = os.path.join(module_full_path, "__manifest__.py")
    with open(manifest_path, "w") as manifest_file:
        manifest_file.write(MANIFEST_TEMPLATE % (today.year, powered_by, module_name, module_description, module_description, module_category))

    # Index html
    index_path = os.path.join(module_full_path, "static", "description", "index.html")
    with open(index_path, "w") as index_file:
        index_file.write(INDEX_TEMPLATE % (today.year, powered_by, module_name, module_description))

    # Module icon
    icon_dest_path = os.path.join(module_full_path, "static", "description", "icon.png")
    shutil.copy(HUROOS_ICON_PATH, icon_dest_path)
