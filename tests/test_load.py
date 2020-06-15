import os
import tempfile
from page_loader.load import (
    create_file_name,
    get_html,
    write_to_file
)


URL = 'https://hexlet.io/courses'


def get_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(path_to_file):
    with open(path_to_file, 'r') as f:
        result = f.read()
    return result


def test_create_file_name():
    assert create_file_name(URL) == 'hexlet-io-courses.html'


def test_get_html(requests_mock):
    expected = read(get_path('data'))
    requests_mock.get(URL, text=expected)
    assert get_html(URL) == expected


def test_write_to_file():
    with tempfile.TemporaryDirectory() as tmp_dir:
        data = read(get_path('data'))
        path = '{}{}'.format(tmp_dir, 'tmp_file')
        write_to_file(path, data)
        assert read(path) == data
