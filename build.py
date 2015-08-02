from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))


class Link(object):
    def __init__(self, title='LinkTitle', address='google.com'):
        self.title = title
        self.address = address


class Project(object):
    def __init__(self, name='Test', download_link='google.com', github_link='github.com', directory='test', pid='tst', links=None):
        self.name = name
        self.download_link = download_link
        self.github_link = github_link
        self.directory = directory
        self.id = pid
        self.links = links or [Link('google', 'google.com')]

        self.margin = 4
        self.height_per_link = 32
        self.extra_height = len(self.links) * self.height_per_link + self.margin * 2


class SocialLink(object):
    def __init__(self, link='', image_path=''):
        self.link = link
        self.image_path = image_path


class Category(object):
    def __init__(self, label, links):
        self.label = label
        self.links = links


class Sidebar(object):
    def __init__(self, categories):
        self.categories = categories


def build():
    my_projects = [
        Project('XSI ZETools', pid='zet', links=[Link('Downloads', 'https://github.com/Schlechtwetterfront/xsizetools/releases'),
                                                 Link('Overview', '/xsizetools'),
                                                 Link('View Source on Github', 'https://github.com/Schlechtwetterfront/xsizetools'),
                                                 Link('GameToast Forum Thread', 'http://gametoast.com/viewtopic.php?f=36&t=26664')]),
        Project('SoftCry', pid='sc', links=[Link('Downloads', 'https://github.com/Schlechtwetterfront/softcry/releases'),
                                            Link('Overview', '/softcry'),
                                            Link('View Source on Github', 'https://github.com/Schlechtwetterfront/softcry'),
                                            Link('CRYDEV Forum Thread', 'http://www.cryengine.com/community/viewtopic.php?f=315&t=102978')]),
        Project('ZE File Formats', links=[Link('Overview', '/ze_filetypes'),
                                          Link('Download Source', 'https://github.com/Schlechtwetterfront/ze_filetypes/archive/gh-pages.zip'),
                                          Link('View Source on Github', 'https://github.com/Schlechtwetterfront/ze_filetypes')])
    ]

    my_socials = [
        SocialLink('https://github.com/Schlechtwetterfront', 'img/github_white.png'),
        SocialLink('https://twitter.com/schlchtwtrfrnt', 'img/twitter_white.png'),
        SocialLink('http://steamcommunity.com/id/andeweget/', 'img/steam_white.png'),
        SocialLink('https://youtube.com/user/andeweget', 'img/youtube_white.png')
    ]

    template = env.get_template('index_template.html')
    with open('index.html', 'w') as filehandle:
        filehandle.write(template.render(page_title='Schlechtwetterfront', social_links=my_socials, projects=my_projects))


build()
