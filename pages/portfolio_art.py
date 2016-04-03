from page_core import *
from pages import portfolio_index as p
import markdown


PAGE = {
    'page_template': 'portfolio_projects.html',
    'path': '',
    'output_file': 'art.html',
    'output_folder': '',
    'page_title': 'Digital Art',
    'use_bright_theme': True,
    'navbar_links': p.PAGE['navbar_links'],
    'home_text': Section(text='''

This page contains some of my digital "art".

    '''),
    'sections': [
        ProjectBrief(title='Star Wars: Battlecry',
                     tags=['2012-2015', p.T_CPP, p.T_SI, p.T_PS, p.T_ZB, p.T_UE],
                     links=[
                         Link('Project Homepage', 'http://www.swbattlecry.com'),
                     ],
                     images=[(
                        Link('Imperial Scout', 'img/art/bc_scout.png', link_name='swbc'),
                        Link('Rebel Pilot', 'img/art/bc_pilot.png', link_name='swbc'),
                        Link('Jawa', 'img/art/jawa.png', link_name='swbc'),
                        Link('Snowtrooper', 'img/art/bc_snowtrooper.png', link_name='swbc'),
                        # Link('Rebel Fleet Trooper', 'img/art/bc_rebelfleettrooper.png'),
                        # Link('Hoth Cave Environment', 'img/art/bc_hoth_cave_01.png'),
                        # Link('Hoth Cave Environment', 'img/art/bc_hoth_cave_02.png'),
                        ),
                     ],
                     text='''
**Star Wars: Battlecry** is a fan project that aims to create an authentic Star Wars shooter. This is some of my older art created
for that project over the years.


#### Tasks

* Modelled and textured most of the characters.
* Designed, modelled and textured some environments.
* Implementation of game modes, items and various other smaller game code features.

        '''),
    ],
}
