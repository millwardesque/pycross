import pytest

from rendering_engine import RenderingEngine
from image import Image


def test_create_renderer():
    r = RenderingEngine.mock_engine(320, 240, 14)
    assert r.width() == 320
    assert r.height() == 240

def test_invalid_screen_size():
    with pytest.raises(ValueError):
        RenderingEngine.mock_engine(-1, 240, 14)

    with pytest.raises(ValueError):
        RenderingEngine.mock_engine(0, 240, 14)

    with pytest.raises(ValueError):
        RenderingEngine.mock_engine(320, -1, 14)

    with pytest.raises(ValueError):
        RenderingEngine.mock_engine(320, 0, 14)

def test_clear_screen():
    r = RenderingEngine.mock_engine(320, 240, 14)
    r.clear()

    assert r.last_command() == { 'name': 'clear' }

def test_end_render():
    r = RenderingEngine.mock_engine(320, 240, 14)
    r.end_render()

    assert r.last_command() == { 'name': 'end_render' }

def test_drawing_static_image():
    test_img = Image('intro_ball.gif', directory='test_assets')
    r = RenderingEngine.mock_engine(320, 240, 14)
    r.draw_static_image(test_img, 5, 3)

    assert r.last_command() == {
        'name': 'draw_static_image',
        'img': test_img,
        'x': 5,
        'y': 3
    }

def test_image_not_found():
    missing_img = Image('test-image')
    r = RenderingEngine.mock_engine(320, 240, 14)

    with pytest.raises(ValueError):
        r.draw_static_image(missing_img, 5, 3)

def test_drawing_text():
    text = 'Test text!'
    r = RenderingEngine.mock_engine(320, 240, 14)
    r.draw_text(text, 50, 25)

    assert r.last_command() == {
        'name': 'draw_text',
        'text': text,
        'x': 50,
        'y': 25,
        'color': None,
    }

def test_drawing_text():
    text = 'Test text!'
    r = RenderingEngine.mock_engine(320, 240, 14)
    r.draw_text(text, 50, 25, color=[255, 0, 0])

    assert r.last_command() == {
        'name': 'draw_text',
        'text': text,
        'x': 50,
        'y': 25,
        'color': [255, 0, 0],
    }

def test_get_font_size():
    font_size = 26
    r = RenderingEngine.mock_engine(320, 240, font_size)
    assert r.font_size() == font_size
