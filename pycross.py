import pygame

from board import Board
from board_renderer import BoardRendererInterface
from rendering_engine import RenderingEngine
from text_board_renderer import TextBoardRenderer

class Pycross:
    _renderer: RenderingEngine = None
    _clock: pygame.time.Clock = None
    _is_running: bool = False
    _board: Board = None
    _board_renderer: BoardRendererInterface = None

    def initialize(self) -> None:
        self._renderer = RenderingEngine.pygame_engine(640, 480, 14)
        self._clock = pygame.time.Clock()
        self._board_renderer = TextBoardRenderer()

        squares = [
            [1, 0, 0],
            [0, 1, 0],
            [1, 0, 1],
            [1, 0, 0],
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
        self._renderer.draw_text(f"FPS: {fps}", 5, 500)

        self._board_renderer.render_board(self._renderer, 0, 0, self._board, is_revealed=False)

        self._renderer.end_render()
