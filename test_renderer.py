import pytest

from renderer import Renderer
from mock_rendering_engine import MockRenderingEngine
from image import Image


def test_create_renderer():
    renderer = Renderer(MockRenderingEngine(320, 240))
    assert renderer.width() == 320
    assert renderer.height() == 240

def test_empty_rendering_engine():
    with pytest.raises(ValueError):
        Renderer(None)

def test_invalid_screen_size():
    with pytest.raises(ValueError):
        Renderer(MockRenderingEngine(-1, 240))

    with pytest.raises(ValueError):
        Renderer(MockRenderingEngine(0, 240))

    with pytest.raises(ValueError):
        Renderer(MockRenderingEngine(320, -1))

    with pytest.raises(ValueError):
        Renderer(MockRenderingEngine(320, 0))

def test_clear_screen():
    engine = MockRenderingEngine(320, 240)
    Renderer(engine).clear()

    assert engine.last_command() == { 'name': 'clear' }

def test_flip_screen():
    engine = MockRenderingEngine(320, 240)
    Renderer(engine).flip()

    assert engine.last_command() == { 'name': 'flip' }

def test_drawing_static_image():
    test_img = Image('test-image')
    engine = MockRenderingEngine(320, 240)
    renderer = Renderer(engine)
    renderer.draw_static_image(test_img, 5, 3)

    assert engine.last_command() == {
        'name': 'draw_static_image',
        'img': test_img,
        'x': 5,
        'y': 3
    }

def test_drawing_text():
    text = 'Test text!'
    engine = MockRenderingEngine(320, 240)
    renderer = Renderer(engine)
    renderer.draw_text(text, 50, 25)

    assert engine.last_command() == {
        'name': 'draw_text',
        'text': text,
        'x': 50,
        'y': 25,
    }
