import pygame
from pygame.locals import *

from lib import utils
from lib.game_parameters import GameParams
from lib.utils import BlocksGenerator, BlocksDrawer

directions = {K_LEFT: (-GameParams.PIXEL_SIZE, 0),
              K_RIGHT: (GameParams.PIXEL_SIZE, 0),
              K_DOWN: (0, GameParams.PIXEL_SIZE)}


def init_game():
    pygame.init()
    screen_tmp = pygame.display.set_mode((GameParams.WINDOW_WIDTH, GameParams.WINDOW_HEIGHT))
    screen_tmp.fill(GameParams.BACKGROUND_COLOR)
    pygame.display.update()
    return screen_tmp


def draw_frame(screen_frame, tiles: list):
    screen_frame.fill(GameParams.BACKGROUND_COLOR)
    BlocksDrawer.draw(screen_frame, tiles)
    pygame.display.flip()


if __name__ == '__main__':
    rect0 = Rect(50, 60, 200, 80)
    rect = rect0.copy()

    screen = init_game()

    blocks = BlocksGenerator.generate(utils.pick_random_figure()["template"])

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key in directions:
                    utils.move_figure(blocks, event.key)
        draw_frame(screen, blocks)

    pygame.quit()
