import pygame
from Constants import Const, Colour, Game


imgR = pygame.transform.scale(pygame.image.load("img\R.jpg"), (Const.cellSize, Const.cellSize))
imgC = pygame.transform.scale(pygame.image.load("img\C.jpg"), (Const.cellSize, Const.cellSize))
imgI = pygame.transform.scale(pygame.image.load("img\I.jpg"), (Const.cellSize, Const.cellSize))
imgL = pygame.transform.scale(pygame.image.load("img\L.jpg"), (Const.cellSize, Const.cellSize))
imgT = pygame.transform.scale(pygame.image.load("img\T.jpg"), (Const.cellSize, Const.cellSize))
imgX = pygame.transform.scale(pygame.image.load("img\X.jpg"), (Const.cellSize, Const.cellSize))
imgO = pygame.transform.scale(pygame.image.load("img\O.jpg"), (Const.cellSize, Const.cellSize))


# DISPLAY ALL THE CELLS
def all_cell():
    for y in range(10):
        for x in range(10):
            cell(x, y)
    pygame.display.update()


# DISPLAY ONE CELL
def cell(x, y):
    Game.screen.blit(pygame.transform.rotate(eval('img'+Game.board[y][x].type), -Game.board[y][x].rotation),
                                            (Const.margin+Const.cellSize*x, Const.margin+Const.cellSize*y))
    grid()
    pygame.display.update()


# DISPLAY GAME GRID
def grid():
    for x in range(Const.margin, Const.margin+Const.cellSize*Const.gameSize+1, Const.cellSize):
        pygame.draw.line(Game.screen, Colour.grey, (x, Const.margin), (x, Const.margin+Const.cellSize*Const.gameSize))

    for y in range(Const.margin, Const.margin+Const.cellSize*Const.gameSize+1, Const.cellSize):
        pygame.draw.line(Game.screen, Colour.grey, (Const.margin, y), (Const.margin+Const.cellSize*Const.gameSize, y))
    pygame.display.update()
