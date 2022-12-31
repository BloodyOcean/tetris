import pygame

import utils
from BlocksDrawer import BlocksDrawer
from GameParameters import GameParams
from TemplateParser import FigureParser


def init_game():
    pygame.init()
    screen = pygame.display.set_mode((GameParams.WINDOW_WIDTH, GameParams.WINDOW_HEIGHT))
    screen.fill(GameParams.BACKGROUND_COLOR)
    pygame.display.update()
    return screen


if __name__ == '__main__':

    screen = init_game()

    BlocksDrawer.draw(screen, utils.pick_random_figure()["template"])

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
