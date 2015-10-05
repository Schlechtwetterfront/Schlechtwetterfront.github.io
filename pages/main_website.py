from page_core import *

PAGE = {
    'page_template': 'index_template.html',
    'path': '',
    'output_file': 'index.html',
    'output_folder': '',
    'page_title': 'Schlechtwetterfront',
    'use_bright_theme': True,
    'social_links': [
        SocialLink('https://github.com/Schlechtwetterfront', 'img/github_white.png'),
        SocialLink('https://twitter.com/schlchtwtrfrnt', 'img/twitter_white.png'),
        SocialLink('http://steamcommunity.com/id/andeweget/', 'img/steam_white.png'),
        SocialLink('https://youtube.com/user/andeweget', 'img/youtube_white.png')
    ],
    'projects': [
        Project('XSI ZETools', pid='zet', links=[
            Link('Downloads', 'https://github.com/Schlechtwetterfront/xsizetools/releases'),
            Link('Overview', '/xsizetools'),
            Link('View Source on GitHub', 'https://github.com/Schlechtwetterfront/xsizetools'),
            Link('GameToast Forum Thread', 'http://gametoast.com/viewtopic.php?f=36&t=26664')
            ],
            subtitle='XSI <> ZeroEngine Pipeline'),
        Project('SoftCry', pid='sc', links=[
            Link('Downloads', 'https://github.com/Schlechtwetterfront/softcry/releases'),
            Link('Overview', '/softcry'),
            Link('View Source on GitHub', 'https://github.com/Schlechtwetterfront/softcry'),
            Link('CRYDEV Forum Thread', 'http://www.cryengine.com/community/viewtopic.php?f=315&t=102978')
            ],
            subtitle='XSI > CRYENGINE Exporter'),
        Project('ZE File Formats', pid='zeff', links=[
            Link('Overview', '/ze_filetypes'),
            Link('Download Source', 'https://github.com/Schlechtwetterfront/ze_filetypes/archive/gh-pages.zip'),
            Link('View Source on GitHub', 'https://github.com/Schlechtwetterfront/ze_filetypes')
            ],
            subtitle='ZeroEngine Format Specification'),
        Project('Personal Info', pid='personal_info', links=[
            Link('E-Mail', 'mailto:schlchtwtrfrnt@gmail.com'),
            Link('GitHub', 'https://github.com/Schlechtwetterfront'),
            Link('Twitter', 'https://twitter.com/schlchtwtrfrnt'),
            Link('YouTube', 'https://youtube.com/user/andeweget'),
            ],
            subtitle='Contact and Social Media')
    ]
}
