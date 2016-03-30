from page_core import *
import markdown


PROGRAMMING_SKILLS = '''
**Programming & Software Development**

* Python
* JavaScript + JQUery
* C++
* C#
* Java
* Lua
* ASP.NET
'''


OTHER_SKILLS = '''
**Miscellaneous**

* <span class="bg-success">Photoshop</span>
* Autodesk Softimage
* Unreal Engine 4
* ZBrush
* xNormal
'''

T_PY = 'Python'
T_SI = 'Autodesk Softimage'
T_ZE = 'ZeroEngine'
T_CE = 'CRYENGINE'
T_PI = 'Plug-in'


GI_MAIL = '<span class="glyphicon glyphicon-envelope" aria-hidden="true"></span>'
MAIL = '{} Mail'.format(GI_MAIL)


PAGE = {
    'page_template': 'portfolio_projects.html',
    'path': '',
    'output_file': 'index.html',
    'output_folder': '',
    'page_title': 'Schlechtwetterfront',
    'use_bright_theme': True,
    'navbar_links': [
        Link('Home', 'index.html'),
        Link('Projects', 'projects.html'),
        Link('Code Snippets', 'snippets.html'),
        Link('Digital Art', 'art.html'),
        # Link('About & Contact', 'about.html')
    ],
    'home_text': Section(text='''

Welcome to my page! I'm a hobby software developer and artist.

Here you can find some of my bigger software projects, smaller code pieces and some art I created.

    '''),
    'sections': [
        ProjectBrief(title='Skills & Contact',
                     links=[
                        Link(MAIL, 'mailto:schlchtwtrfrnt@gmail.com'),
                        Link('Github', 'https://github.com/Schlechtwetterfront'),
                        Link('Twitter', 'https://twitter.com/schlchtwtrfrnt'),
                        Link('YouTube', 'https://youtube.com/user/andeweget'),
                        Link('ArtStation', 'https://www.artstation.com/artist/schlechtwetterfront'),
                     ],
                     text='''

#### Key

<span class="label label-success label-lg">Experienced</span>
<span class="label label-info label-lg">I Know My Way Around It</span>
<span class="label label-warning label-lg">I've Used It For Some Time</span>



#### Software Development

<span class="label label-success label-lg">Python</span>
<span class="label label-info label-lg">JavaScript / JQuery</span>
<span class="label label-info label-lg">C#</span>
<span class="label label-info label-lg">Lua</span>
<span class="label label-warning label-lg">C++</span>
<span class="label label-warning label-lg">ASP.NET MVC</span>
<span class="label label-warning label-lg">Java</span>

#### Miscellaneous

<span class="label label-success label-lg">Adobe Photoshop</span>
<span class="label label-success label-lg">Autodesk Softimage</span>
<span class="label label-info label-lg">UnrealEngine 4</span>
<span class="label label-info label-lg">ZBrush</span>
<span class="label label-info label-lg">xNormal</span>
        '''),
#         ProjectBrief(title='Contact',
#                      text='''
# <a href="mailto:benedikt.f.schatz@gmail.com">Mail</a>
# <a href="https://github.com/Schlechtwetterfront">Github</a>
# <a href="https://twitter.com/schlchtwtrfrnt">Twitter</a>
# <a href="https://youtube.com/user/andeweget">YouTube</a>
#         '''),
    ],
}
