import abc
from image import Image

DEFAULT_FONT_SIZE = 14

class RenderingEngine(metaclass=abc.ABCMeta):
    _width: int = None
    _height: int = None
    _font_size: int = None

    def mock_engine(width: int, height: int, font_size: int):
        from mock_rendering_engine import MockRenderingEngine
        return MockRenderingEngine(width, height, font_size)

    def pygame_engine(width: int, height: int, font_size: int):
        from pygame_rendering_engine import PygameRenderingEngine
        return PygameRenderingEngine(width, height, font_size)

    def __init__(self, width: int, height: int, font_size: int):
        if width < 1 or height < 1:
            raise ValueError(f"Width and height of screen must each be > 1: Provided dimensions: ({width}, {height})")

        self._width = width
        self._height = height
        self._font_size = font_size

    def width(self) -> int:
        return self._width

    def height(self) -> int:
        return self._height

    def font_size(self) -> int:
        return self._font_size

    @abc.abstractmethod
    def clear(self):
        pass

    @abc.abstractmethod
    def end_render(self):
        pass

    @abc.abstractmethod
    def draw_static_image(self, img: Image, x: int, y: int):
        pass

    @abc.abstractmethod
    def draw_text(self, text: str, x: int, y: int, color: list=None):
        pass

    @abc.abstractmethod
    def get_text_width(self, text, render_horizontal: bool=True):
        pass

    @abc.abstractmethod
    def get_text_height(self, text, render_horizontal: bool=True):
        pass

