from page_core import *

PAGE = {
		'page_template': 'project_index.html',
		'path': '../',
		'output_file': 'index.html',
		'output_folder': 'softcry',
		'page_title': 'SoftCry',
		'categories': [
			Category('Downloads', [
							   Link('Releases', 'https://github.com/Schlechtwetterfront/softcry/releases')
							   ]),
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
			Section('Main Info', 'main_info', True, False, False, '''
CryENGINE 3 exporter for Softimage.  

* Intuitive workflow for exporting.
* No special setup required for a basic export.
* CryEngine specific material properties directly interface with Softimage materials, so there is no restriction on the type of shaders/materials you can use in XSI.
* Batch export.
* Support for different grid-units (1 unit = 1cm or 1m).
* Animation export + straight forward animation clip editor.
'''),
			Section('Download & Installation', 'download_installation', True, False, False, '''
Check the sidebar for a link to the releases page on GitHub.
    
To install SoftCry, unzip the downloaded archive into  
**C:/users/%user%/Autodesk/Softimage_%version%/Addons/**  
OR  
**C:/users/%user%/Softimage/Softimage_%version%/Addons/**.  
Make sure you use this path and not the factory addon path.  

If you have any Softimage version up to (and including) 2010 you need to install
[python](http://www.python.org/ftp/python/2.6.6/python-2.6.6.msi)
and
[pywin32](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20217/pywin32-217.win32-py2.6.exe/download).
If python and pywin32 was installed correctly it should look something like
[this](installed_python.jpg).  
''')
		]
	}
