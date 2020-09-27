from collections import OrderedDict
from json import load, dump
from pathlib import Path
import os


def build_msh_hierarchy():
    base_dir = Path(os.path.realpath(__file__)).parent

    chunks = None
    with open(base_dir / 'mshformat.json') as stream:
        chunks = load(stream, object_pairs_hook=OrderedDict)

    hier = OrderedDict()
    for key, chunk in chunks.items():
        if chunk['name'] == 'ExampleChunk' \
           or chunk['category'] in set(['Other', 'Deprecated']):
            continue

        chunk['simple_children'] = OrderedDict()
        chunk['container_children'] = OrderedDict()
        chunk['all_children'] = OrderedDict()
        chunk['has_containers'] = False

        for chunk_key in chunk['children']:
            if chunks.get(chunk_key) and chunks[chunk_key]['children']:
                chunk['container_children'][chunk_key] = chunks[chunk_key]
                chunk['has_containers'] = True
            elif chunks.get(chunk_key) and not chunks[chunk_key]['children']:
                chunk['simple_children'][chunk_key] = chunks[chunk_key]

            if chunks.get(chunk_key):
                chunk['all_children'][chunk_key] = chunks[chunk_key]
            else:
                chunk['all_children'][chunk_key] = {
                    'all_children': [],
                    'name': chunk_key,
                    'no_link': True,
                }
                print(chunk_key)
        if not chunk['parent']:
            hier[key] = chunk

    with open(base_dir / 'mshhierarchy.json', 'w') as stream:
        dump(hier, stream)


if __name__ == '__main__':
    build_msh_hierarchy()
