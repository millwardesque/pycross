import abc

from board import Board
from rendering_engine import RenderingEngine

class BoardRendererInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render_board(self, renderer: RenderingEngine, x: int, y: int, board: Board, is_revealed: bool):
        pass
