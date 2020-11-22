import pytest

from pygame_rendering_engine import PygameRenderingEngine

def test_get_text_width():
    font_size = 14
    r = PygameRenderingEngine(320, 240, font_size)
    text = 'TEST!'
    expected_width = 40  # Determined by running this as a failing test first. Awkard :s
    expected_vertical_width = 9 # Determined by running this as a failing test first. Awkard :s

    assert r.get_text_width(text) == expected_width
    assert r.get_text_width(text, render_horizontal=False) == expected_vertical_width

def test_get_text_height():
    font_size = 14
    r = PygameRenderingEngine(320, 240, font_size)
    text = 'TEST!'

    # These values were determined by running this as a failing test
    # first. Awkward :s
    expected_height = 16
    expected_vertical_height = 80

    assert r.get_text_height(text) == expected_height
    assert r.get_text_height(text, render_horizontal=False) == expected_vertical_height
