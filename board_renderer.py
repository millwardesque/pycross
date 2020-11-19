### TODO
# Renders solved board
# Renders unsolved board
# Renders numerical solutions
# Renders column of numbers
# Renders row of numbers

### DONE

from board import Board


class BoardRenderer:
    def __init__(self):
        pass

    def _get_grid_dimensions(self, board):
        columns = self._get_axis_size(board.columns())
        rows = self._get_axis_size(board.rows())
        return [columns, rows]

    def _get_axis_size(self, axis):
        axis_element_count = len(axis)

        longest_element = 0
        largest_element = 0
        for element in axis:
            if len(str(element)) > longest_element:
                longest_element = len(str(element))
            if element > largest_element:
                largest_element = element

        element_size = longest_element + 1
        definition_size = axis_element_count * element_size
        grid_size = largest_element * 2
        return definition_size + grid_size
