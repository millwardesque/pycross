from image import Image
from rendering_engine import RenderingEngine


class Renderer:
    def __init__(self, rendering_engine: RenderingEngine):
        if rendering_engine is None:
            raise ValueError("Rendering engine passed to renderer is None")

        self.rendering_engine = rendering_engine

    def width(self) -> int:
        return self.rendering_engine.width()

    def height(self) -> int:
        return self.rendering_engine.height()

    def clear(self):
        self.rendering_engine.clear()

    def draw_static_image(self, image: Image, x: int, y: int):
        self.rendering_engine.draw_static_image(image, x, y)

    def draw_text(self, text: str, x: int, y: int):
        self.rendering_engine.draw_text(text, x, y)
