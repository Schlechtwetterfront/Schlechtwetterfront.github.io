from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

import os, time


def build():
    import pages
    num_errors = 0
    for page in pages.PAGES:
        # try:
        build_template(page)
        # except Exception as e:
        # print(e)
        # print('\n\tBuild failed!')
        # num_errors += 1
    if num_errors > 0:
        print('\n\t> Build finished ({num_errors} errors).'.format(num_errors=num_errors))
        input('Any key to continue.')
    else:
        print('\n\t> Build successful!')
        time.sleep(0.5)


def build_template(data):
    print('Building page \'{title}\'.'.format(title=data.get('page_title')))
    template = env.get_template(data.get('page_template'))
    path = os.path.join(os.getcwd(), data.get('output_folder'), data.get('output_file'))
    with open(path, 'w') as filehandle:
        filehandle.write(template.render(**data))


build()
