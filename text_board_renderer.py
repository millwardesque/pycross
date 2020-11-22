from board import Board
from board_renderer import BoardRendererInterface
from rendering_engine import RenderingEngine


class TextBoardRenderer(BoardRendererInterface):

    def render_board(self, renderer: RenderingEngine, x: int, y: int, board: Board, is_revealed: bool):
        pass

    def render_row_definition(self, renderer: RenderingEngine, x: int, y: int, board: Board, row: int):
        row_def = board.get_definition('row', row)
        row_def_str = self._row_definition_as_str(row_def)
        renderer.draw_text(row_def_str, x, y)

    def render_column_definition(self, renderer: RenderingEngine, x: int, y: int, board: Board, column: int):
        column_def = board.get_definition('column', column)
        for i in column_def:
            i_str = str(i)
            renderer.draw_text(i_str, x, y)
            y += renderer.get_text_height(i_str)

    #def render_grid_unsolved(self, renderer: Renderer, x: int, y: int, board: Board):
    #    pass
    #
    #def render_grid_revealed(self, renderer: Renderer, x: int, y: int, board: Board):
    #    pass
    #
    #def render_markers(self, renderer: Renderer, x: int, y: int, board: Board):
    #    pass

    def _row_definition_as_str(self, row_definition: list) -> str:
        return ' '.join([str(x) for x in row_definition])

    def get_row_definition_width(self, renderer: RenderingEngine, board: Board, row: int) -> int:
        row_def = board.get_definition('row', row)
        row_def_str = self._row_definition_as_str(row_def)
        return renderer.get_text_width(row_def_str)

    def get_row_definition_height(self, renderer: RenderingEngine, board: Board, row: int) -> int:
        row_def = board.get_definition('row', row)
        row_def_str = self._row_definition_as_str(row_def)
        return renderer.get_text_height(row_def_str)