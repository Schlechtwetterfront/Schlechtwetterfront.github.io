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
    def __init__(self, title, links):
        self.title = title
        self.links = links


class Sidebar(object):
    def __init__(self, categories):
        self.categories = categories


class Section(object):
    def __init__(self, title, name, text):
        self.title = title
        self.name = name
        self.text = text


class ListSection(object):
    def __init__(self, title, name, items):
        self.title = title
        self.name = name
        self.items = items

    @property
    def text(self):
        items = ['<ul>']
        items.extend( ['<li>{0}</li>'.format(item) for item in self.items] )
        items.append('</ul>')
        return '\n'.join(items)
    
