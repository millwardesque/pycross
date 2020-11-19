import pytest

from board import Board, SquareMarking


def test_board_with_valid_grid():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)
    assert test_board.width() == 3
    assert test_board.height() == 2

    assert test_board.width() == len(test_board._marking_grid[0])
    assert test_board.height() == len(test_board._marking_grid)

def test_board_with_empty_or_none_grid():
    with pytest.raises(ValueError):
        Board(None)

    with pytest.raises(ValueError):
        Board([])

    with pytest.raises(ValueError):
        Board([[]])

def test_get_square():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)
    assert test_board.square(1, 1) == 1
    assert test_board.square(0, 1) == 0

def test_get_square_out_of_range():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)

    with pytest.raises(IndexError):
        test_board.square(2, 0)

    with pytest.raises(IndexError):
        test_board.square(0, 3)

    with pytest.raises(IndexError):
        test_board.square(-1, 0)

    with pytest.raises(IndexError):
        test_board.square(0, -1)

def test_get_square_marking():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)
    assert test_board.square_marking(1, 1) == SquareMarking.UNMARKED

def test_get_square_marking_out_of_range():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)

    with pytest.raises(IndexError):
        test_board.square_marking(2, 0)

    with pytest.raises(IndexError):
        test_board.square_marking(0, 3)

    with pytest.raises(IndexError):
        test_board.square_marking(-1, 0)

    with pytest.raises(IndexError):
        test_board.square_marking(0, -1)

def test_mark_square():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)

    test_board.mark_square(1, 0, SquareMarking.YES)
    assert test_board.square_marking(1, 0) == SquareMarking.YES

    test_board.mark_square(0, 0, SquareMarking.NOTED)
    assert test_board.square_marking(0, 0) == SquareMarking.NOTED

def test_clear_square():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)

    test_board.mark_square(1, 0, SquareMarking.YES)
    test_board.clear_square(1, 0)
    assert test_board.square_marking(1, 0) == SquareMarking.UNMARKED

def test_is_square_correct():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)

    test_board.clear_square(0, 0)
    assert test_board.is_square_matched(0, 0) == False
    test_board.mark_square(0, 0, SquareMarking.YES)
    assert test_board.is_square_matched(0, 0) == True
    test_board.mark_square(0, 0, SquareMarking.NOTED)
    assert test_board.is_square_matched(0, 0) == False

    test_board.clear_square(0, 1)
    assert test_board.is_square_matched(0, 1) == True
    test_board.mark_square(0, 1, SquareMarking.YES)
    assert test_board.is_square_matched(0, 1) == False
    test_board.mark_square(0, 1, SquareMarking.NOTED)
    assert test_board.is_square_matched(0, 1) == True

def test_is_row_complete():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)

    assert test_board.is_row_complete(1) == False
    test_board.mark_square(1, 1, SquareMarking.YES)
    assert test_board.is_row_complete(1) == True

def test_is_board_complete():
    squares = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    test_board = Board(squares)

    assert test_board.is_board_complete() == False
    test_board.mark_square(0, 0, SquareMarking.YES)
    test_board.mark_square(0, 2, SquareMarking.YES)
    test_board.mark_square(1, 1, SquareMarking.YES)
    assert test_board.is_board_complete() == True

def test_board_row_definition():
    squares = [
        [1, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
    ]
    test_board = Board(squares)

    assert test_board.get_definition('row', 0) == [2]
    assert test_board.get_definition('row', 1) == [1]
    assert test_board.get_definition('row', 2) == [1, 1]

def test_board_column_definition():
    squares = [
        [1, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
    ]
    test_board = Board(squares)

    assert test_board.get_definition('column', 0) == [1, 1]
    assert test_board.get_definition('column', 1) == [1]
    assert test_board.get_definition('column', 2) == [2]
