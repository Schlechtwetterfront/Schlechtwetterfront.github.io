from page_core import *
import json
from collections import OrderedDict

MSHFORMAT = None
with open('mshformat.json', 'r') as file_handler:
	MSHFORMAT = json.load(file_handler, object_pairs_hook=OrderedDict)



def get_structure(chunk):
	structure = ['Data Type | Size (bytes) | Description',
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
	links = ['See also:']
	if chunk.get('links'):
		for link in chunk.get('links'):
			links.append('[{}]({})'.format(link.get('name'), link.get('link')))
		links.append('\n')
		links = ' | '.join(links)
	else:
		links = ''
	return links


def chunks_to_sections():
	sections = []
	for chunk_key in MSHFORMAT.keys():
		chunk = MSHFORMAT[chunk_key]

		if chunk.get('parent'):
			parent = '[{name}](#{name})'.format(name=chunk.get('parent'))
		else:
			parent = '-'

		if chunk.get('children'):
			children = ' '.join('[{name}](#{id})'.format(name=n, id=n.replace('.', '_')) for n in chunk.get('children'))
		else:
			children = '-'
		necessity = chunk.get('necessity')
		description = chunk.get('description') + '\n'

		structure = get_structure(chunk)
		links = get_links(chunk)
		

		section = Section('## {}'.format(chunk_key), chunk_key.replace('.', '_'), True, True, False, '''
{description}
{links}

Parent	|	Children	|	Necessity	|
--------|---------------|---------------|
{parent}|	{children}	|	{necessity}	|

{structure}
'''.format(parent=parent, children=children, necessity=necessity, description=description, links=links, structure=structure))
		sections.append(section)
	
	return sections


def get_chunk_nav_links():
	links = []
	for chunk_key in MSHFORMAT.keys():
		chunk = MSHFORMAT[chunk_key]
		link = Link(chunk.get('name'), '#{}'.format(chunk_key.replace('.', '_')))
		links.append(link)
	return links

PAGE = {
		'page_template': 'project_index.html',
		'path': '../',
		'output_file': 'msh.html',
		'output_folder': 'ze_filetypes',
		'page_title': 'ZE File Formats - .MSH',
		'categories': [
			Category('Navigation', [
							   Link('Back', 'index.html'),
							   Link('Back to Top', '#'),
							   ]),
			Category('Chunks', get_chunk_nav_links()),
			Category('Personal', [
							   Link('Personal Homepage', 'http://schlechtwetterfront.github.io/')])
		],
		'sections': chunks_to_sections()
	}
