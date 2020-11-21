import pytest

import renderer
from rendering_engine import RenderingEngine
from image import Image


def test_create_renderer():
    r = renderer.Renderer(RenderingEngine.mock_engine(320, 240))
    assert r.width() == 320
    assert r.height() == 240

def test_empty_rendering_engine():
    with pytest.raises(ValueError):
        renderer.Renderer(None)

def test_invalid_screen_size():
    with pytest.raises(ValueError):
        renderer.Renderer(RenderingEngine.mock_engine(-1, 240))

    with pytest.raises(ValueError):
        renderer.Renderer(RenderingEngine.mock_engine(0, 240))

    with pytest.raises(ValueError):
        renderer.Renderer(RenderingEngine.mock_engine(320, -1))

    with pytest.raises(ValueError):
        renderer.Renderer(RenderingEngine.mock_engine(320, 0))

def test_clear_screen():
    engine = RenderingEngine.mock_engine(320, 240)
    renderer.Renderer(engine).clear()

    assert engine.last_command() == { 'name': 'clear' }

def test_end_render():
    engine = RenderingEngine.mock_engine(320, 240)
    renderer.Renderer(engine).end_render()

    assert engine.last_command() == { 'name': 'end_render' }

def test_drawing_static_image():
    test_img = Image('intro_ball.gif', directory='test_assets')
    engine = RenderingEngine.mock_engine(320, 240)
    r = renderer.Renderer(engine)
    r.draw_static_image(test_img, 5, 3)

    assert engine.last_command() == {
        'name': 'draw_static_image',
        'img': test_img,
        'x': 5,
        'y': 3
    }

def test_drawing_text():
    text = 'Test text!'
    engine = RenderingEngine.mock_engine(320, 240)
    r = renderer.Renderer(engine)
    r.draw_text(text, 50, 25)

    assert engine.last_command() == {
        'name': 'draw_text',
        'text': text,
        'x': 50,
        'y': 25,
    }

def test_image_not_found():
    missing_img = Image('test-image')
    engine = RenderingEngine.mock_engine(320, 240)
    r = renderer.Renderer(engine)

    with pytest.raises(ValueError):
        r.draw_static_image(missing_img, 5, 3)
