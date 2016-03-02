

# SIZE CONSTANTS
class Const(object):
    cellSize = 40
    gameSize = 10       # size in number of cell
    margin = 80         # between grid and windows
    windowHeight = margin*2 + cellSize*gameSize
    windowLength = margin*2 + cellSize*gameSize


# COLOR CONSTANTS
class Colour(object):
    darkGrey = (40, 40, 40)
    grey = (70, 70, 70)


# GAME VARIABLE
class Game(object):
    # Will be initialized later
    screen = None       # Pygame Surface of the window
    board = None        # Array of the game
