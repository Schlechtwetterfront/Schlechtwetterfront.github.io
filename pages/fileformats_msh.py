from page_core import *
import json
from collections import OrderedDict


CHUNKS_GENERAL = ('HEDR', 'SHVO', 'MSH2', 'SINF', 'FRAM', 'CAMR', 'NAME', 'BBOX')
CHUNKS_MATERIALS = ('MATL', 'MATD', 'MATD.DATA', 'ATRB', 'TX0D', 'PRFX')
CHUNKS_MODELS = ('MODL', 'MTYP', 'MNDX', 'PRNT', 'FLGS', 'TRAN', 'SWCI', 'GEOM', 'ENVL')
CHUNKS_SEGMENTS = ('SEGM', 'SHDW', 'MATI', 'POSL', 'NRML', 'UV0L', 'CLRL', 'CLRB', 'WGHT' 'NDXL', 'NDXT', 'STRP', 'VLTB', 'VLTL')
CHUNKS_CLOTH = ('CLTH', 'CTEX', 'CPOS', 'CUV0', 'FIDX', 'FWGT', 'CMSH', 'SPRS', 'CPRS', 'BPRS', 'COLL')
CHUNKS_ANIMATION = ('SKL2', 'BLN2', 'ANM2', 'CYCL', 'KFR3')
CHUNKS_DEPRECATED = ('FINF', 'LGTP', 'LGTI', 'LGTS', 'FOGD')

CHUNK_CATEGORIES = (
    CHUNKS_GENERAL,
    CHUNKS_MATERIALS,
    CHUNKS_MODELS,
    CHUNKS_SEGMENTS,
    CHUNKS_CLOTH,
    CHUNKS_ANIMATION,
    CHUNKS_DEPRECATED
)


MSHFORMAT = None
with open('mshformat.json', 'r') as file_handler:
    MSHFORMAT = json.load(file_handler, object_pairs_hook=OrderedDict)



def get_structure(chunk):
    structure = ['### Structure',
                 'Data Type | Size (bytes) | Description',
                 '----------|--------------|------------']
    if chunk.get('structure'):
        for row in chunk.get('structure'):
            row_items = []
            if 'int' in row[0] or 'float' in row[0]:
                structure.append('{}{{: .red}} | {} | {}'.format(*row))
            elif 'byte' in row[0]:
                structure.append('{}{{: .orange}} | {} | {}'.format(*row))
            elif 'string' in row[0]:
                structure.append('{}{{: .green}} | {} | {}'.format(*row))
            else:
                structure.append('{} | {} | {}'.format(*row))
        structure.append(' ')
        structure = '\n'.join(structure)
    else:
        structure = ''
    return structure


def get_links(chunk):
    links = ['**See also:**']
    if chunk.get('links'):
        for link in chunk.get('links'):
            links.append('[{}]({})'.format(link.get('name'), link.get('link')))
        links.append('\n')
        links = '&nbsp;&nbsp;&nbsp;'.join(links)
    else:
        links = ''
    return links


def get_additional_tables(chunk):
    tables_data = chunk.get('additional_tables')
    tables = []
    for table_data in tables_data:
        table = []
        for index, row in enumerate(table_data.get('table')):
            table.append(' | '.join(row))
            if index == 0:
                table.append('{}  '.format(' | '.join(['---'] * len(row))))
        tables.append('### {}'.format(table_data.get('name')))
        tables.append('\n'.join(table))
    return '\n\n'.join(tables)


def chunks_to_sections():
    info_section = Section('Overview', 'overview', True, False, False, '''
This page lists all .MSH file chunks. In the .MSH file these chunks are organized in a hierarchy with [HEDR](#HEDR){: .bordered .block} (header) being the first chunk and branching out
from there (as visualized in the sidebar navigation).  

Some of these chunks are exclusive to certain versions of the engine (_Star Wars: The Clone Wars_ and before, _Star Wars: Battlefront_ and _Star Wars: Battlefront II_) or deprecated completely.
Most notably Cloth Simulation ([CLTH](#CLTH){: .bordered .block} and children) being limited to _Star Wars: Battlefront II_.
        ''')
    sections = [info_section]
    for chunk_key in MSHFORMAT.keys():
        chunk = MSHFORMAT[chunk_key]

        if chunk.get('parent'):
            parent = '[{name}](#{name}){{: .bordered .block}}'.format(name=chunk.get('parent'))
        else:
            parent = '-'

        if chunk.get('children'):
            children = ' '.join('[{name}](#{id}){{: .bordered .block}}'.format(name=n, id=n.replace('.', '_')) for n in chunk.get('children'))
        else:
            children = '-'
        necessity = chunk.get('necessity')
        description = chunk.get('description') + '\n'

        structure = get_structure(chunk)
        links = get_links(chunk)

        if chunk.get('additional_tables'):
            additional_table = get_additional_tables(chunk)
        else:
            additional_table = ''

        collapsed = True
        if chunk.get('name') == 'ExampleChunk':
            collapsed = False

        brief_description = chunk.get('brief_description') or ''

        section = Section('{name}'.format(name=chunk_key, brief=brief_description), chunk_key.replace('.', '_'), True, collapsed, False, '''
### Description
{description}

Parent  |   Children    |   Necessity   |
--------|---------------|---------------|
{parent}|   {children}  |   {necessity} |

{links}

{structure}

{additional_table}
'''.format(parent=parent, children=children, necessity=necessity, description=description, links=links, structure=structure, additional_table=additional_table))
        sections.append(section)
    
    return sections


def get_chunk_nav_links():
    links = []
    for chunk_key in MSHFORMAT.keys():
        chunk = MSHFORMAT[chunk_key]
        link_title = chunk.get('name')
        if chunk.get('hierarchy_level') > 0:
            indent_string = ['<indent-child></indent-child>'] * chunk.get('hierarchy_level')
            indent_string = ''.join(indent_string)
            link_title = '{}<text-container>{}</text-container>'.format(indent_string, chunk.get('name'))
        link = Link(link_title, '#{}'.format(chunk_key.replace('.', '_')), link_class='rectangle-button rectangle-button-semi rectangle-button-msh')
        links.append(link)
    return links


def get_navbar_links():
    categories = [
        Category('General Chunks', is_sidebar_category=False),
        Category('Material Chunks', is_sidebar_category=False),
        Category('Model Chunks', is_sidebar_category=False),
        Category('Geometry Chunks', is_sidebar_category=False),
        Category('Cloth Chunks', is_sidebar_category=False),
        Category('Animation Chunks', is_sidebar_category=False),
        Category('Deprecated Chunks', is_sidebar_category=False),
    ]
    for chunk_key in MSHFORMAT.keys():
        chunk = MSHFORMAT[chunk_key]
        link_title = chunk.get('name')
        link = Link(link_title, '#{}'.format(chunk_key.replace('.', '_')))
        for index, category in enumerate(CHUNK_CATEGORIES):
            if link_title in category:
                categories[index].links.append(link)
                break
    return categories


def get_categories():
    categories = [
        Category('Navigation', [
            Link('Overview', '#overview'),
            Link('Back', 'index.html', LINK_INTERNAL),
            ], is_navbar_category=False),
        Category('Chunks', get_chunk_nav_links(), True, is_navbar_category=False)
    ]
    categories.extend(get_navbar_links())
    return categories


PAGE = {
    'page_template': 'project_index.html',
    'path': '../',
    'output_file': 'msh.html',
    'output_folder': 'ze_filetypes',
    'page_title': 'ZE File Formats - .MSH',
    'use_bright_theme': True,
    'fixed_categories': [

    ],
    'categories': get_categories(),
    'sections': chunks_to_sections()
}
