from page_core import *
from pages import portfolio_index as p
import markdown


PAGE = {
    'page_template': 'portfolio_projects.html',
    'path': '',
    'output_file': 'snippets.html',
    'output_folder': '',
    'page_title': 'Code Snippets',
    'use_bright_theme': True,
    'navbar_links': p.PAGE['navbar_links'],
    'home_text': Section(text='''

This page lists some of the more notable code snippets from my [Github Gists](https://gist.github.com/Schlechtwetterfront).

    '''),
    'sections': [
        ProjectBrief(title='Vertex Color Changer',
                     tags=[p.T_PY, p.T_SI, p.T_PI],
                     links=[Link('Github Gist', 'https://gist.github.com/Schlechtwetterfront/6896743')],
                     images=[[Link('Dialog', 'img/gist_vertcolchanger.png'), Link('Process', 'img/vertcol_anim.gif')]],
                     text='''
A small python plug-in for (X)SI. Let's you set RGB or HSV colors. This applies the colors to the first vertex color cluster it finds for
every model in the current selection. If it doesn't find a cluster it can create one if you check the Create Cluster option. I created
this very basic script for a friend who needed to eliminate baked AO from the vertex colors but wanted to keep the light colors in.


#### Usage

This adds a sub menu to Animate > Get > Property called "Edit Vertex Colors". Choose "Set Vertex Colors" from there and adjust
settings in the UI as you like.
        '''),
        ProjectBrief(title='Select Points by Envelope Weight',
                     tags=[p.T_PY, p.T_SI, p.T_PI],
                     links=[Link('Github Gist', 'https://gist.github.com/Schlechtwetterfront/73124aa70db53398383c')],
                     images=[[Link('Process', 'img/select_env_weights.gif')]],
                     text='''
Selects all points on object ```enveloped_mesh``` which have a weight value for ```deformer``` bigger than ```weight_threshold```.


#### Usage

This command needs to be executed from script.

Open the script editor ("Scroll" button in the bottom panel of the Softimage UI or <kbd>Alt + 4</kbd>) and call

```Application.SelectPointsByEnvelopeWeight(enveloped_mesh, deformer, weight_threshold)```

For python, VB/JS don't need the ```Application.```.

* ```enveloped_mesh```: The object's SI name (i.e. 'character_torso').
* ```deformer```: The deformer object's SI name (i.e. 'bone_spine_a').
* ```weight_threshold```: Weight percentage threshold (0-100).
        '''),
    ],
}
