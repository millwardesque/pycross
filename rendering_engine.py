from image import Image


class RenderingEngine:
    _width: int = None
    _height: int = None

    def mock_engine(width: int, height: int):
        from mock_rendering_engine import MockRenderingEngine
        return MockRenderingEngine(width, height)

    def pygame_engine(width: int, height: int):
        from pygame_rendering_engine import PygameRenderingEngine
        return PygameRenderingEngine(width, height)

    def __init__(self, width: int, height: int):
        if width < 1 or height < 1:
            raise ValueError(f"Width and height of screen must each be > 1: Provided dimensions: ({width}, {height})")

        self._width = width
        self._height = height

    def width(self) -> int:
        return self._width

    def height(self) -> int:
        return self._height

    def clear(self):
        raise NotImplementedError("RenderingEngine base class doesn't implement this method")

    def end_render(self):
        raise NotImplementedError("RenderingEngine base class doesn't implement this method")

    def draw_static_image(self, img: Image, x: int, y: int):
        raise NotImplementedError("RenderingEngine base class doesn't implement this method")

    def draw_text(self, text: str, x: int, y: int):
        raise NotImplementedError("RenderingEngine base class doesn't implement this method")