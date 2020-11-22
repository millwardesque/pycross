from image import Image
import os
from rendering_engine import RenderingEngine


class MockRenderingEngine(RenderingEngine):
    _last_command: object = None


    def __init__(self, width: int, height: int, font_size: int):
        super().__init__(width, height, font_size)

    def clear(self):
        self._last_command = {
            'name': 'clear'
        }

    def end_render(self):
        self._last_command = {
            'name': 'end_render'
        }

    def draw_static_image(self, img: Image, x: int, y: int):
        if not os.path.isfile(img.full_path()):
            raise ValueError(f"Image at {img.full_path()} doesn't exist")

        self._last_command = {
            'name': 'draw_static_image',
            'img': img,
            'x': x,
            'y': y,
        }

    def draw_text(self, text: str, x: int, y: int, color: list=None):
        self._last_command = {
            'name': 'draw_text',
            'text': text,
            'x': x,
            'y': y,
            'color': color
        }

    def last_command(self) -> str:
        return self._last_command