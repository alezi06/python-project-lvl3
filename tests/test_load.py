import os
import tempfile
from page_loader.load import (
    create_file_name,
    get_content,
    write_to_file
)


URL1 = 'https://hexlet.io/courses'
URL2 = 'https://hexlet.io'
URL3 = '/assets/main.css'


def get_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(path_to_file):
    with open(path_to_file, 'rb') as f:
        result = f.read()
    return result


def test_create_file_name():
    assert create_file_name(URL1) == 'hexlet-io-courses'
    assert create_file_name(URL2) == 'hexlet-io'
    assert create_file_name(URL3) == 'assets-main.css'


def test_get_content(requests_mock):
    expected = read(get_path('data'))
    requests_mock.get(URL1, content=expected)
    assert get_content(URL1) == expected


def test_write_to_file():
    with tempfile.TemporaryDirectory() as tmp_dir:
        data = read(get_path('data'))
        path = '{}{}'.format(tmp_dir, 'tmp_file')
        write_to_file(path, data, 'wb')
        assert read(path) == data
