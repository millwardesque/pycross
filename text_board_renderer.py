from board import Board
from board_renderer import BoardRendererInterface
from rendering_engine import RenderingEngine


class TextBoardRenderer(BoardRendererInterface):

    def render_board(self, renderer: RenderingEngine, board_x: int, board_y: int, board: Board, is_revealed: bool):
        max_row_width = self.get_max_row_definition_width(renderer, board)
        max_column_height = self.get_max_column_definition_height(renderer, board)

        column_x = max_row_width
        for column in range(0, board.width()):
            column_y_offset = max_column_height - self.get_column_definition_height(renderer, board, column)
            # @DEBUG print(f"[{column}] {column_y_offset} = {max_column_height} - {self.get_column_definition_height(renderer, board, column)}")
            self.render_column_definition(renderer, column_x, board_y + column_y_offset, board, column)
            column_x += self.get_column_definition_width(renderer, board, column)

        row_y = max_column_height
        for row in range(0, board.height()):
            row_x_offset = max_row_width - self.get_row_definition_width(renderer, board, row)
            self.render_row_definition(renderer, row_x_offset, row_y, board, row)
            row_y += self.get_row_definition_height(renderer, board, row)

    def render_row_definition(self, renderer: RenderingEngine, x: int, y: int, board: Board, row: int):
        row_def = board.get_definition('row', row)
        row_def_str = self._definition_as_str(row_def)
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

    def _definition_as_str(self, definition: list) -> str:
        return ' '.join([str(x) for x in definition])

    def get_row_definition_width(self, renderer: RenderingEngine, board: Board, row: int) -> int:
        definition = board.get_definition('row', row)
        definition_str = self._definition_as_str(definition)
        return renderer.get_text_width(definition_str)

    def get_row_definition_height(self, renderer: RenderingEngine, board: Board, row: int) -> int:
        definition = board.get_definition('row', row)
        definition_str = self._definition_as_str(definition)
        return renderer.get_text_height(definition_str)

    def get_column_definition_width(self, renderer: RenderingEngine, board: Board, column: int) -> int:
        definition = board.get_definition('column', column)
        definition_str = self._definition_as_str(definition)
        return renderer.get_text_width(definition_str, render_horizontal=False)

    def get_column_definition_height(self, renderer: RenderingEngine, board: Board, column: int) -> int:
        definition = board.get_definition('column', column)
        definition_str = self._definition_as_str(definition)
        return renderer.get_text_height(definition_str, render_horizontal=False)

    def get_max_row_definition_width(self, renderer: RenderingEngine, board: Board) -> int:
        max_width = 0
        for row in range(0, board.height()):
            width = self.get_row_definition_width(renderer, board, row)
            if width > max_width:
                max_width = width

        return max_width

    def get_max_column_definition_height(self, renderer: RenderingEngine, board: Board) -> int:
        max_height = 0
        for column in range(0, board.width()):
            height = self.get_column_definition_height(renderer, board, column)
            if height > max_height:
                max_height = height

        return max_height
