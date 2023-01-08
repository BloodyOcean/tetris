import pygame
from pygame.locals import *

from lib import utils
from lib.game_parameters import GameParams
from lib.utils import BlocksGenerator, BlocksDrawer
from models.figure import Figure


def init_game():
    pygame.init()
    screen_tmp = pygame.display.set_mode((GameParams.WINDOW_WIDTH, GameParams.WINDOW_HEIGHT))
    pygame.display.set_caption('Tetris')
    screen_tmp.fill(GameParams.BACKGROUND_COLOR)
    pygame.display.update()
    return screen_tmp


def draw_frame(screen_frame, tiles: list):
    screen_frame.fill(GameParams.BACKGROUND_COLOR)
    BlocksDrawer.draw(screen_frame, tiles)
    pygame.display.flip()


def draw_frame_merged(screen_frame, figure):
    screen_frame.fill(GameParams.BACKGROUND_COLOR)
    BlocksDrawer.draw_rectangle(screen_frame, figure)
    pygame.display.flip()


if __name__ == '__main__':

    screen = init_game()
    blocks = BlocksGenerator.generate(utils.pick_random_figure()["template"])
    f = Figure(screen, blocks)

    pygame.display.update()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in utils.directions:
                    f.move(event.key)
                if event.key == K_UP:
                    f.rotate()

        screen.fill(GameParams.BACKGROUND_COLOR)
        screen.blit(f.image, (f.x, f.y))

        pygame.display.update()

    pygame.quit()
