import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


TAG_ATTRS = {'link': 'href', 'script': 'src', 'img': 'src'}


def create_file_name(url):
    u = urlparse(url)
    path, ext = os.path.splitext(u.path)
    file_name = re.sub(r'\W', '-', u.netloc + path)
    return '{}{}'.format(file_name.strip('-'), ext)


def get_content(url):
    r = requests.get(url)
    return r.content


def write_to_file(path, content, flag='w'):
    with open(path, flag) as f:
        f.write(content)


def change_links(page, dir_name):
    soup = BeautifulSoup(page, 'html.parser')
    links = []
    for tag in soup.find_all(['link', 'script', 'img']):
        attr = TAG_ATTRS[tag.name]
        value = tag.get(attr)
        if value and not value.startswith(('http', '//')):
            links.append(value)
            tag[attr] = os.path.join(dir_name, create_file_name(value))
    return links, str(soup)


def save_resources(links, path, url):
    u = urlparse(url)
    for link in links:
        content = get_content(f'{u.scheme}://{u.netloc}{link}')
        write_to_file(path, content, 'wb')


def load_page(url, output):
    content = get_content(url)
    name = create_file_name(url)
    file_name = f'{name}.html'
    dir_name = f'{name}_files'
    os.makedirs(os.path.join(output, dir_name), exist_ok=True)
    links, data = change_links(content, dir_name)
    write_to_file(os.path.join(output, file_name), data)
    save_resources(links, os.path.join(output, dir_name), url)
