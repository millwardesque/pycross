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

    def end_render(self):
        self.rendering_engine.end_render()

    def draw_static_image(self, image: Image, x: int, y: int):
        self.rendering_engine.draw_static_image(image, x, y)

    def draw_text(self, text: str, x: int, y: int):
        self.rendering_engine.draw_text(text, x, y)

if __name__ == '__main__':
    import os
    from pygame_rendering_engine import PygameRenderingEngine
    import pygame

    renderer = Renderer(PygameRenderingEngine(320, 240))
    clock = pygame.time.Clock()
    img = Image('intro_ball.gif', directory='assets')
    while 1:
        clock.tick()

        fps = round(clock.get_fps(), 2)
        renderer.clear()
        renderer.draw_text(f"FPS: {fps}", 5, 5)
        renderer.draw_static_image(img, 100, 100)
        renderer.end_render()
