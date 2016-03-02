from Constants import Const, Game
import Display


def click(x, y):
    x = (x - Const.margin) // Const.cellSize
    y = (y - Const.margin) // Const.cellSize
    Game.board[y][x].turn()
    Display.cell(x, y)
