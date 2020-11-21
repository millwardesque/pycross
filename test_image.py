import pytest

from image import Image


def test_filename_only():
    img = Image('test_image.png')

    assert img.name() == 'test_image.png'
    assert img.directory() == ''
    assert img.full_path() == 'test_image.png'

def test_filename_and_directory():
    img = Image('test_image.png', directory='test_dir')

    assert img.name() == 'test_image.png'
    assert img.directory() == 'test_dir'
    assert img.full_path() == 'test_dir/test_image.png'