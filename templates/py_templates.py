"""Python files templates"""


MANIFEST_TEMPLATE: str = """# Copyright %s - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
# Powered by %s

{
    'name': "%s",
    'summary': \"\"\"%s\"\"\",
    'description': \"\"\"%s\"\"\",

    'author': "Huroos - www.huroos.com",
    'website': "https://www.huroos.com",
    'category': "%s",
    'version': "0.1",
    'license': "LGPL-3",

    'depends': [],

    'data': [

    ]
}
"""
