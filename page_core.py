import markdown

LINK_NORMAL = 'LINK_NORMAL'
LINK_INTERNAL = 'LINK_INTERNAL'
LINK_EXTERNAL = 'LINK_EXTERNAL'
LINK_DOWNLOAD = 'LINK_DOWNLOAD'
LINK_VIDEO = 'LINK_VIDEO'

MARKDOWN_EXTENSIONS = ['markdown.extensions.extra', 'markdown.extensions.fenced_code', 'markdown.extensions.tables']

class Link(object):
    def __init__(self, title='LinkTitle', address='google.com', link_type=LINK_NORMAL, link_class='rectangle-button rectangle-button-semi', link_name=''):
        self.title = title
        self.address = address
        self.link_type = link_type
        self.link_class = link_class
        self.link_name = link_name

        self.link_type = LINK_NORMAL

        self.is_video = link_type == LINK_VIDEO


class Project(object):
    def __init__(self, name='Test', download_link='google.com', github_link='github.com', directory='test', pid='tst', links=None, subtitle=''):
        self.name = name
        self.download_link = download_link
        self.github_link = github_link
        self.directory = directory
        self.id = pid
        self.links = links or [Link('google', 'google.com')]
        self.subtitle = subtitle

        self.margin = 4
        self.height_per_link = 32
        # Calculates the amount of space the links require.
        self.extra_height = len(self.links) * self.height_per_link + self.margin * 2
        self.extra_hover_size = 25


class SocialLink(object):
    def __init__(self, link='', image_path=''):
        self.link = link
        self.image_path = image_path


class Category(object):
    def __init__(self, title, links=None, is_scrollable=False, is_navbar_category=True, is_sidebar_category=True):
        self.title = title
        self.links = links or []
        self.is_scrollable = is_scrollable

        self.is_navbar_category = is_navbar_category
        self.is_sidebar_category = is_sidebar_category


class Sidebar(object):
    def __init__(self, categories):
        self.categories = categories


class Section(object):
    def __init__(self, title='', name='', is_collapsable=False, is_collapsed=False, is_long=False, text=''):
        self.raw_title = title
        self.name = name
        self.raw_text = text
        self.is_collapsable = is_collapsable
        self.is_collapsed = is_collapsed
        self.is_long = is_long

    @property
    def text(self):
        return markdown.markdown(self.raw_text, extensions=MARKDOWN_EXTENSIONS)

    @property
    def title(self):
        return markdown.markdown(self.raw_title, extensions=MARKDOWN_EXTENSIONS)


class ProjectBrief:
    def __init__(self, title='', text='', tags=None, images=None, links=None):
        self.title = title
        self.text = text
        self.tags = tags or []
        self.images = images or []
        self.links = links or []

    def markdown(self, attribute):
        return markdown.markdown(getattr(self, attribute), extensions=MARKDOWN_EXTENSIONS)

    def has_links(self):
        if len(self.links):
            return True
        return False 

    def has_images(self):
        if len(self.images):
            return True
        return False
    


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
    
