import os
from pycross import Pycross

game = Pycross()
game.initialize()

while game.is_running():
    game.run()
