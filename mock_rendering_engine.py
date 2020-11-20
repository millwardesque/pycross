from image import Image
from rendering_engine import RenderingEngine


class MockRenderingEngine(RenderingEngine):
    _last_command: object = None

    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def clear(self):
        self._last_command = {
            'name': 'clear'
        }

    def draw_static_image(self, img: Image, x: int, y: int):
        self._last_command = {
            'name': 'draw_static_image',
            'img': img,
            'x': x,
            'y': y,
        }

    def draw_text(self, text: str, x: int, y: int):
        self._last_command = {
            'name': 'draw_text',
            'text': text,
            'x': x,
            'y': y,
        }

    def last_command(self) -> str:
        return self._last_command