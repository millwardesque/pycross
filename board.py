from enum import Enum


class SquareMarking(Enum):
    UNMARKED = 1
    YES = 2
    NOTED = 3

    def __str__(self):
        if self == SquareMarking.UNMARKED:
            return '.'
        elif self == SquareMarking.YES:
            return 'X'
        elif self == SquareMarking.NOTED:
            return '?'
        else:
            return str(self.value)


class Board:
    _grid: list = None,
    _marking_grid: list = None

    def __init__(self, grid: list):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            raise ValueError("Board grid must have at least 1 row and 1 column")

        self._grid = grid
        self._marking_grid = []

        for row in range(0, self.height()):
            self._marking_grid.append([SquareMarking.UNMARKED] * self.width())

    def width(self) -> int:
        return len(self._grid[0])

    def height(self) -> int:
        return len(self._grid)

    def square(self, row: int, column: int):
        if row < 0 or column < 0:
            raise IndexError(f"Row and column indexes must be greater than 0: ({row}, {column})")

        return self._grid[row][column]

    def square_marking(self, row: int, column: int):
        if row < 0 or column < 0:
            raise IndexError(f"Row and column indexes must be greater than 0: ({row}, {column})")

        return self._marking_grid[row][column]

    def mark_square(self, row: int, column: int, marking: SquareMarking):
        self._marking_grid[row][column] = marking

    def clear_square(self, row: int, column: int):
        self._marking_grid[row][column] = SquareMarking.UNMARKED

    def is_square_matched(self, row, column):
        square = self.square(row, column)
        marking = self.square_marking(row, column)

        if square == 0:
            return marking == SquareMarking.UNMARKED or marking == SquareMarking.NOTED
        elif square == 1:
            return marking == SquareMarking.YES
        else:
            raise ValueError(f"Grid square ({row}, {column}) has an unsupported value {self._grid[row][column]}")

    def is_row_complete(self, row):
        for column in range(0, self.width()):
            if not self.is_square_matched(row, column):
                return False

        return True

    def is_board_complete(self):
        for row in range(0, self.height()):
            if not self.is_row_complete(row):
                return False

        return True

    def get_definition(self, axis: str, index: int):
        definition = []

        in_sequence = False
        sequence_length = 0

        squares = []
        if axis == 'row':
            for column in range(0, self.width()):
                squares.append(self.square(index, column))
        elif axis == 'column':
            for row in range(0, self.height()):
                squares.append(self.square(row, index))
        else:
            raise ValueError(f"Unable to get definition for axis {axis}: axis must be 'row' or 'column'")

        for square in squares:
            if square == 1:
                if in_sequence:
                    sequence_length += 1
                else:
                    in_sequence = True
                    sequence_length = 1
            elif square == 0:
                if in_sequence:
                    in_sequence = False
                    definition.append(sequence_length)
                    sequence_length = 0

        # If we finish the row and are still in a sequence, close it.
        if in_sequence:
            in_sequence = False
            definition.append(sequence_length)
            sequence_length = 0

        return definition

    def grid_as_str(self):
        grid_string = ""
        for row in range(0, self.height()):
            for column in range(0, self.width()):
                grid_string += str(self.square(row, column))

                if column < self.width() - 1:
                    grid_string += " "
            grid_string += "\n"
        return grid_string

    def markings_as_str(self):
        marking_string = ""
        for row in range(0, self.height()):
            for column in range(0, self.width()):
                marking_string += str(self.square_marking(row, column))

                if column < self.width() - 1:
                    marking_string += " "

            marking_string += "\n"
        return marking_string

    def __str__(self):
        grid_string = "GRID:\n"
        grid_string += self.grid_as_str()

        marking_string = "MARKINGS:\n"
        marking_string += self.markings_as_str()

        definition_string = "DEFINITIONS:\n"
        definition_string += "Rows:\n"
        for i in range(0, self.height()):
            definition_string += str(test_board.get_definition('row', i))
            definition_string += "\n"

        definition_string += "Columns:\n"
        for i in range(0, self.width()):
            definition_string += str(test_board.get_definition('column', i))
            definition_string += " "

        status_string = "STATUS:\n"
        status_string += "Is complete: " + str(self.is_board_complete())
        status_string += "\n"

        return grid_string + "\n" + marking_string + "\n" + status_string + "\n" + definition_string


if __name__ == '__main__':
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)
    test_board.mark_square(0, 0, SquareMarking.YES)
    test_board.mark_square(1, 1, SquareMarking.YES)
    print(test_board)
