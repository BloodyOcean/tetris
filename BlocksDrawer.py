import random

import pygame
from pygame.rect import Rect

from GameParameters import GameParams


class BlocksDrawer:
    @staticmethod
    def draw(surface, pattern: list) -> list:
        lst = [pygame.draw.rect(surface,
                                random.choice(GameParams.PALETTE),
                                Rect(j * GameParams.PIXEL_SIZE,
                                     i * GameParams.PIXEL_SIZE,
                                     GameParams.PIXEL_SIZE,
                                     GameParams.PIXEL_SIZE))
               for j in range(len(pattern[0]))
               for i in range(len(pattern)) if pattern[i][j] == 1]

        return lst
