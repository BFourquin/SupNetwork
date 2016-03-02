import random
import copy
from Cell import Cell
from Constants import Game


def array(level=1):

    random.seed()

    if level == 1:
        level_map = [['C', 'C', 'O', 'O', 'O', 'O', 'O', 'L', 'C', 'C'],
                     ['L', 'T', 'I', 'I', 'L', 'O', 'O', 'I', 'O', 'I'],
                     ['O', 'O', 'O', 'O', 'I', 'O', 'O', 'I', 'O', 'I'],
                     ['O', 'O', 'O', 'L', 'L', 'O', 'O', 'T', 'T', 'L'],
                     ['C', 'I', 'I', 'X', 'R', 'O', 'O', 'I', 'L', 'C'],
                     ['L', 'I', 'I', 'T', 'I', 'I', 'L', 'T', 'L', 'O'],
                     ['I', 'O', 'O', 'O', 'O', 'O', 'L', 'L', 'I', 'O'],
                     ['I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'I', 'O'],
                     ['I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'I', 'O'],
                     ['C', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'L', 'C']]

    for y in range(10):
        for x in range(10):
                # conversion to an array of cells objects
                level_map[y][x] = Cell(level_map[y][x], x, y, 90*random.randint(0, 3))

    Game.board = copy.deepcopy(level_map)
