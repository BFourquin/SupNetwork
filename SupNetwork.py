import sys
import pygame
from pygame.locals import *

from Constants import Const, Colour, Game
import Init
import Display
import Action


if __name__ == '__main__':

    # PYGAME INIT
    pygame.init()
    Game.screen = pygame.display.set_mode((Const.windowHeight, Const.windowLength))
    Game.screen.fill(Colour.darkGrey)
    pygame.display.set_caption('SupNetwork')
    clock = pygame.time.Clock()

    # DISPLAY
    Init.array()
    Display.all_cell()

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            clock.tick(30)

            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                if Const.margin < x < Const.margin+Const.cellSize*Const.gameSize \
                        and Const.margin < y < Const.margin+Const.cellSize*Const.gameSize:
                    Action.click(x, y)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
