from page_core import *

PAGE = {
		'page_template': 'project_index.html',
		'path': '../',
		'output_file': 'msh.html',
		'output_folder': 'ze_filetypes',
		'page_title': 'ZE File Formats - .MSH',
		'categories': [
			Category('General Info', [
							   Link('Main Info', '#main_info'),
							   Link('Download & Installation', '#download_installation'),
							   ]),
			Category('Other Resources', [
							   Link('View on GitHub', 'https://github.com/Schlechtwetterfront/softcry'),
							   Link('View Thread on CRYDEV', 'http://www.cryengine.com/community/viewtopic.php?f=315&t=102978'),
							   Link('Hardbody Animations (Video)', 'http://www.youtube.com/watch?v=2Rt3B8h5EvE')
							   ]),
			Category('Personal', [
							   Link('Personal Homepage', 'http://schlechtwetterfront.github.io/')])
		],
		'sections': [
			Section('## Main Info', 'main_info', True, False, False, '''
---
'''),
			Section('## Download & Installation', 'download_installation', True, False, False, '''
---
''')
		]
	}
