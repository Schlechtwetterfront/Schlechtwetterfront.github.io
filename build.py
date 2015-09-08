from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

import os, shutil


def build():
    import pages
    for page in pages.PAGES:
        build_template(page)

def build_template(data):
    print('Building page \'{title}\'.'.format(title=data.get('page_title')))
    template = env.get_template(data.get('page_template'))
    path = os.path.join(os.getcwd(), data.get('output_folder'), data.get('output_file'))
    with open(path, 'w') as filehandle:
        filehandle.write(template.render(**data))


build()
