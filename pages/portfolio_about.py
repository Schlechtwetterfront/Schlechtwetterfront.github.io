from page_core import *
from pages import portfolio_index
import markdown


PAGE = {
    'page_template': 'portfolio_projects.html',
    'path': '',
    'output_file': 'about.html',
    'output_folder': '',
    'page_title': 'About & Contact',
    'use_bright_theme': True,
    'navbar_links': portfolio_index.PAGE['navbar_links'],
    'home_text': Section(text='''



    '''),
    'sections': [
    ],
}
