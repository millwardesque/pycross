import pytest

from renderer import Renderer
from rendering_engine import RenderingEngine
from image import Image


def test_create_renderer():
    r = Renderer(RenderingEngine.mock_engine(320, 240))
    assert r.width() == 320
    assert r.height() == 240

def test_empty_rendering_engine():
    with pytest.raises(ValueError):
        Renderer(None)

def test_invalid_screen_size():
    with pytest.raises(ValueError):
        Renderer(RenderingEngine.mock_engine(-1, 240))

    with pytest.raises(ValueError):
        Renderer(RenderingEngine.mock_engine(0, 240))

    with pytest.raises(ValueError):
        Renderer(RenderingEngine.mock_engine(320, -1))

    with pytest.raises(ValueError):
        Renderer(RenderingEngine.mock_engine(320, 0))

def test_clear_screen():
    r = Renderer(RenderingEngine.mock_engine(320, 240))
    r.clear()

    assert r.rendering_engine().last_command() == { 'name': 'clear' }

def test_end_render():
    r = Renderer(RenderingEngine.mock_engine(320, 240))
    r.end_render()

    assert r.rendering_engine().last_command() == { 'name': 'end_render' }

def test_drawing_static_image():
    test_img = Image('intro_ball.gif', directory='test_assets')
    r = Renderer(RenderingEngine.mock_engine(320, 240))
    r.draw_static_image(test_img, 5, 3)

    assert r.rendering_engine().last_command() == {
        'name': 'draw_static_image',
        'img': test_img,
        'x': 5,
        'y': 3
    }

def test_image_not_found():
    missing_img = Image('test-image')
    r = Renderer(RenderingEngine.mock_engine(320, 240))

    with pytest.raises(ValueError):
        r.draw_static_image(missing_img, 5, 3)

def test_drawing_text():
    text = 'Test text!'
    r = Renderer(RenderingEngine.mock_engine(320, 240))
    r.draw_text(text, 50, 25)

    assert r.rendering_engine().last_command() == {
        'name': 'draw_text',
        'text': text,
        'x': 50,
        'y': 25,
        'color': None,
    }

def test_drawing_text():
    text = 'Test text!'
    r = Renderer(RenderingEngine.mock_engine(320, 240))
    r.draw_text(text, 50, 25, color=[255, 0, 0])

    assert r.rendering_engine().last_command() == {
        'name': 'draw_text',
        'text': text,
        'x': 50,
        'y': 25,
        'color': [255, 0, 0],
    }
