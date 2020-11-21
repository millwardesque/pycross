import pytest

from pycross import Pycross


def test_init():
    game = Pycross()
    game.initialize()
    assert game.is_ready() == True

def test_run():
    game = Pycross()
    game.initialize()
    game.run()
