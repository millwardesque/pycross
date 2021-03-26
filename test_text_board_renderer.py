import pytest

from board import Board
from rendering_engine import RenderingEngine
from text_board_renderer import TextBoardRenderer

DEFAULT_FONT_SIZE = 10

def test_row_definition_width():
     squares = [
         [1, 0, 1],
         [0, 1, 0],
     ]
     test_board = Board(squares)
     text_renderer = TextBoardRenderer()
     r = RenderingEngine.pygame_engine(640, 480, DEFAULT_FONT_SIZE)

     expected_width = r.get_text_width("1 1")
     assert text_renderer.get_row_definition_width(r, test_board, 0) == expected_width

def test_row_definition_height():
     squares = [
         [1, 0, 1],
         [0, 1, 0],
     ]
     test_board = Board(squares)
     text_renderer = TextBoardRenderer()
     r = RenderingEngine.pygame_engine(640, 480, DEFAULT_FONT_SIZE)

     expected_height = r.get_text_height("1 1")
     assert text_renderer.get_row_definition_height(r, test_board, 0) == expected_height

def test_column_definition_width():
     squares = [
         [1, 0, 1],
         [0, 1, 0],
     ]
     test_board = Board(squares)
     text_renderer = TextBoardRenderer()
     r = RenderingEngine.pygame_engine(640, 480, DEFAULT_FONT_SIZE)

     expected_width = r.get_text_width("1 1", render_horizontal=False)
     assert text_renderer.get_column_definition_width(r, test_board, 0) == expected_width

def test_column_definition_height():
     squares = [
         [1, 0, 1],
         [0, 1, 0],
         [1, 1, 0],
         [0, 1, 0],
         [1, 1, 0],
     ]
     test_board = Board(squares)
     text_renderer = TextBoardRenderer()
     r = RenderingEngine.pygame_engine(640, 480, DEFAULT_FONT_SIZE)

     expected_height = r.get_text_height("1 1 1", render_horizontal=False)
     assert text_renderer.get_column_definition_height(r, test_board, 0) == expected_height

def test_max_row_definition_width():
    squares = [
         [0, 1, 0],
         [1, 0, 1],
    ]
    test_board = Board(squares)
    text_renderer = TextBoardRenderer()
    r = RenderingEngine.pygame_engine(640, 480, DEFAULT_FONT_SIZE)

    expected_width = r.get_text_width("1 1")
    assert text_renderer.get_max_row_definition_width(r, test_board) == expected_width

def test_max_row_definition_width():
    squares = [
         [0, 1, 1],
         [1, 0, 0],
         [1, 1, 0],
         [1, 0, 0],
         [1, 1, 0],
     ]
    test_board = Board(squares)
    text_renderer = TextBoardRenderer()
    r = RenderingEngine.pygame_engine(640, 480, DEFAULT_FONT_SIZE)

    expected_height = r.get_text_height("1 1 1", render_horizontal=False)
    assert text_renderer.get_max_column_definition_height(r, test_board) == expected_height
