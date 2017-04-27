'''
    Builds the static webpage from yaml, jinja templates and scss.
'''

import os
from collections import OrderedDict
from sassutils import builder
from glob import glob
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
from yaml import load as lyaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


DEFAULT_TEMPLATE = 'default.html.j2'

MARKDOWN_EXTRAS = [
    'markdown.extensions.extra',
]


def build():
    build_html()
    build_styles()


def build_html():
    env = Environment(loader=FileSystemLoader('templates'))
    register_filters(env)
    # Pages are stored in yaml docs. Go through all of them and compile them
    # into html.
    global_config = None
    with open('pages/global.yaml') as stream:
        global_config = lyaml(stream, Loader=Loader)

    page_paths = glob('pages/*.yaml')
    for page_path in page_paths:
        if 'global' in page_path:
            continue
        page = None
        with open(page_path, 'r') as stream:
            page = lyaml(stream, Loader=Loader)

        if page.get('resources'):
            for res in page['resources']:
                fn = None
                if res['type'] == 'json':
                    from json import load

                    def fn(stream):
                        return load(stream, object_pairs_hook=OrderedDict)
                elif res['type'] == 'yaml':
                    def fn(stream):
                        return lyaml(f, Loader=Loader)

                with open(res['path']) as f:
                    page[res['key']] = fn(f)

        page['global'] = global_config
        template = env.get_template(page.get('template', DEFAULT_TEMPLATE))
        out_path = os.path.join(os.getcwd(), page.get('out'))
        output = template.render(**page)
        with open(out_path, 'w') as stream:
            stream.write(output)


def build_styles():
    builder.build_directory('css/', '../css/')
    for filepath in glob('../css/*.scss.css'):
        full_path = os.path.join(os.getcwd(), filepath)
        stripped_path = full_path.replace('.scss.', '.')
        if os.path.isfile(stripped_path):
            os.remove(stripped_path)
        os.rename(full_path, stripped_path)


def register_filters(env):
    env.filters['markdown'] = markdown_filter


def markdown_filter(s):
    return markdown(s, extensions=MARKDOWN_EXTRAS) if s else ''


if __name__ == '__main__':
    build()
