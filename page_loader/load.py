import os
import re
import requests


def create_file_name(url):
    temp = '-'.join(url.split('/')[2:])
    file_name = re.sub(r'\W', '-', temp)
    return '{}.html'.format(file_name)


def get_html(url):
    req = requests.get(url)
    return req.text


def write_to_file(path, html):
    with open(path, 'w') as f:
        f.write(html)


def load_page(url, directory):
    html = get_html(url)
    sep = os.path.sep
    path = '{}{}{}'.format(directory, sep, create_file_name(url))
    write_to_file(path, html)
