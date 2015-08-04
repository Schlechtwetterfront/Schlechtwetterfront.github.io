from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

import os, shutil

FOLDERS = ['css', 'js', 'img', 'fonts']


def build():
    import website
    for page in website.pages:
        build_template(page)

def build_template(data):
    template = env.get_template(data.get('page_template'))
    print(os.getcwd())
    path = os.path.join(os.getcwd(), data.get('output_folder'), data.get('output_file'))
    with open(path, 'w') as filehandle:
        filehandle.write(template.render(**data))

    return
    if data.get('output_folder'):
        for folder in FOLDERS:
            shutil.copytree(os.path.join(os.getcwd(), folder), os.path.join(os.getcwd(), data.get('output_folder'), folder))


build()
