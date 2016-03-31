from page_core import *
from pages import portfolio_index as p
import markdown


PAGE = {
    'page_template': 'portfolio_projects.html',
    'path': '',
    'output_file': 'projects.html',
    'output_folder': '',
    'page_title': 'Projects',
    'use_bright_theme': True,
    'navbar_links': p.PAGE['navbar_links'],
    'home_text': Section(text='''

This page contains all my (public) notable projects from my [Github](https://github.com/Schlechtwetterfront).

    '''),
    'sections': [
        ProjectBrief(title='XSIZETools',
                     tags=['2011-', p.T_PY, p.T_SI, p.T_PI, p.T_ZE],
                     links=[
                         Link('Project Homepage', '/xsizetools/'),
                         Link('Releases', 'https://github.com/Schlechtwetterfront/xsizetools/releases'),
                         Link('Github', 'https://github.com/Schlechtwetterfront/xsizetools/'),
                         Link('Gametoast Thread', 'http://gametoast.com/viewtopic.php?f=36&t=26664'),
                     ],
                     images=[
                         (Link('Export Dialog', 'img/zet_export.png'),
                         Link('Import Dialog', 'img/zet_import.png'),
                         Link('Import Settings', 'img/zet_import_settings.png'),
                         Link('Cloth Edit', 'img/zet_cloth.png'),
                         Link('Material Manager', 'img/zet_matman.png'),),
                     ],
                     text='''
XSIZETools is an addon for Autodesk Softimage. It adds support to export & import ZeroEngine (Star Wars: Battlefront I & II) .msh model/animation files.


#### Tasks

* Gathering geometry, material and animation data for export to .msh with Softimage's scripting interface and C++ SDK.
* Reading .msh geometry, material and animation data to feed it back to Softimage's interfaces and rebuild the model for editing.
* Converting between .msh and segmented .json for easy text-file editing.
* UI design for all dialogs with Softimage's scripting UI system.
* Reverse-engineering of big parts of the .msh file format structure.
        '''),
        ProjectBrief(title='SoftCry',
                     tags=['2012-2014', p.T_PY, p.T_SI, p.T_PI, p.T_CE],
                     links=[
                         Link('Project Homepage', '/softcry/'),
                         Link('Releases', 'https://github.com/Schlechtwetterfront/softcry/releases'),
                         Link('Github', 'https://github.com/Schlechtwetterfront/softcry/'),
                         Link('CryDev Thread', 'http://www.cryengine.com/community/viewtopic.php?f=315&t=102978'),
                     ],
                     images=[
                        (Link('Export Dialog', 'img/sc_export.png'),
                         Link('Export Settings', 'img/sc_export_settings.png'),
                         Link('Anim Clip Editor', 'img/sc_animclips.png'),
                         Link('Material Library Editor', 'img/sc_matlib.png'),
                         Link('Misc Tools', 'img/sc_misctools.png'),
                         Link('Settings Dialog', 'img/sc_settings.png'),
                         ),
                     ],
                     text='''
SoftCry is an addon for Autodesk Softimage. It modifies and adds to the output of the Crosswalk Collada (.dae) exporter to add special functionality for
the CRYENGINE resource compiler.


#### Tasks

* Modifying output of the Crosswalk Collada exporter by adding CRYENGINE-specific flags, adjusting nodes and replacing materials.
* Export and import of material libraries.
* Support for CRYENGINE-specific material settings.
* Creating, editing and exporting animation clips.
* UI design for all dialogs with Softimage's scripting UI system.
        '''),
        ProjectBrief(title='TER22',
                     tags=['2013-', p.T_PY, p.T_ZE],
                     links=[
                         Link('Github', 'https://github.com/Schlechtwetterfront/ter22/'),
                     ],
                     text='''
This is a parser and converter for ZeroEngine terrain file formats (.ter and .xxw).


#### Tasks

* Reverse-engineering of big parts of the .ter and .xxw file formats.
* Parser code.
        '''),
        ProjectBrief(title='ZeroEngine File Formats',
                     tags=['2011-', p.T_PY, p.T_ZE],
                     links=[
                         Link('Project Homepage', '/ze_filetypes/'),
                         Link('Github', 'https://github.com/Schlechtwetterfront/ze_filetypes/'),
                     ],
                     text='''
This is a collection of documentation on some of ZeroEngine's proprietary file formats. It contains documentation for the .msh, .ter and .xxw file formats, all 
used in ZeroEngine.
        '''),
    ],
}
