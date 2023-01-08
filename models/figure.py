import pygame

from lib import utils
from lib.game_parameters import GameParams
from lib.utils import directions, get_merged_tiles


class Figure:
    tiles = None
    x = None
    y = None
    image = None

    def __init__(self, parent, lst: list):
        self.tiles = lst
        merged = get_merged_tiles(lst)
        self.x = merged.x
        self.y = merged.y
        self.parent = parent
        self.image = pygame.Surface.subsurface(self.parent, (self.x, self.y, merged.width, merged.height)).copy()
        self.draw()

    def move(self, key) -> None:
        v = directions[key]
        self.x += v[0]
        self.y += v[1]

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, GameParams.ROTATION_ANGLE)

    def draw(self):
        utils.BlocksDrawer.draw(self.image, self.tiles)
