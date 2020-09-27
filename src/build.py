'''
    Builds the static webpage from yaml, jinja templates and scss.
'''

import os
from os import PathLike
from pathlib import Path
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
    base_dir = Path(os.path.realpath(__file__)).parent

    build_html(base_dir)
    build_styles(base_dir)


def build_html(base_dir: Path):
    env = Environment(loader=FileSystemLoader(str(base_dir / 'templates')))
    register_filters(env)
    # Pages are stored in yaml docs. Go through all of them and compile them
    # into html.
    global_config = None
    with open(base_dir / 'pages/global.yaml') as stream:
        global_config = lyaml(stream, Loader=Loader)

    page_paths = base_dir.glob('pages/*.yaml')
    for page_path in page_paths:
        if 'global.yaml' in page_path.parts:
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

                with open(base_dir / res['path']) as f:
                    page[res['key']] = fn(f)

        page['global'] = global_config

        template = env.get_template(page.get('template', DEFAULT_TEMPLATE))
        out_path = base_dir / page.get('out')
        output = template.render(**page)

        os.makedirs(out_path.resolve().parent, exist_ok=True)

        with open(out_path, 'w') as stream:
            stream.write(output)


def build_styles(base_dir: Path):
    out_dir = base_dir.parent / 'css'
    builder.build_directory(str(base_dir / 'css'), str(out_dir))

    for filepath in out_dir.glob('*.scss.css'):
        full_path = out_dir / filepath
        stripped_path = str(full_path).replace('.scss.', '.')

        if os.path.isfile(stripped_path):
            os.remove(stripped_path)

        os.rename(full_path, stripped_path)


def register_filters(env):
    env.filters['markdown'] = markdown_filter


def markdown_filter(s):
    return markdown(s, extensions=MARKDOWN_EXTRAS) if s else ''


if __name__ == '__main__':
    build()
