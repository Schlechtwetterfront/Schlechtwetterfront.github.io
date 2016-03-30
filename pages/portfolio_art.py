from page_core import *
from pages import portfolio_index
import markdown


PAGE = {
    'page_template': 'portfolio_projects.html',
    'path': '',
    'output_file': 'art.html',
    'output_folder': '',
    'page_title': 'Digital Art',
    'use_bright_theme': True,
    'navbar_links': portfolio_index.PAGE['navbar_links'],
    'home_text': Section(text='''

This page contains some of my better "art".

    '''),
    'sections': [
        ProjectBrief(title='TEST', text='''
TEXT
        '''),
    ],
}
