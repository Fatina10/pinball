import re
from grid import grid
from bumper import Bumper
from balls import Balls
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    g = grid()
    b = Bumper()
    c = Balls()

    g.gridSize_def()
    g.grid_def()

    b.bumper_input()

    c.balls_specs()

