import pygame

from board import Board
from rendering_engine import RenderingEngine


class Pycross:
    _renderer: RenderingEngine = None
    _clock: pygame.time.Clock = None
    _is_running: bool = False
    _board: Board = None

    def initialize(self) -> None:
        self._renderer = RenderingEngine.pygame_engine(320, 240, 14)
        self._clock = pygame.time.Clock()

        squares = [
            [1, 0, 1],
            [0, 1, 0],
        ]
        self._board = Board(squares)

        self._is_running = self.is_ready()

    def is_running(self) -> bool:
        return self._is_running

    def is_ready(self) -> bool:
        renderer_ready = self._renderer is not None
        clock_ready = self._clock is not None
        board_ready = self._board is not None

        return renderer_ready and clock_ready and board_ready

    def run(self):
        self._clock.tick()
        fps = round(self._clock.get_fps(), 2)

        self._renderer.clear()
        self._renderer.draw_text(f"FPS: {fps}", 5, 5)
        self._renderer.end_render()
