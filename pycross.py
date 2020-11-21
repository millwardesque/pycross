import pygame
from renderer import Renderer
from rendering_engine import RenderingEngine


class Pycross:
    _renderer: Renderer = None
    _clock: pygame.time.Clock = None


    def initialize(self) -> None:
        self._renderer = Renderer(RenderingEngine.pygame_engine(320, 240))
        self._clock = pygame.time.Clock()

    def is_ready(self) -> bool:
        renderer_ready = self._renderer is not None
        clock_ready = self._clock is not None

        return renderer_ready and clock_ready

    def run(self):
        self._clock.tick()
        fps = round(self._clock.get_fps(), 2)

        self._renderer.clear()
        self._renderer.draw_text(f"FPS: {fps}", 5, 5)
        self._renderer.end_render()
