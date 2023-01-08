import json
import math
import random
from functools import reduce

import pygame
from pygame.locals import *

from lib.game_parameters import GameParams

directions = {K_LEFT: (-GameParams.PIXEL_SIZE, 0),
              K_RIGHT: (GameParams.PIXEL_SIZE, 0),
              K_DOWN: (0, GameParams.PIXEL_SIZE)}


class BlocksDrawer:
    @staticmethod
    def draw(surface, tiles: list) -> list:
        lst = [BlocksDrawer.draw_rectangle(surface, tile) for tile in tiles]

        return lst

    @staticmethod
    def draw_rectangle(surface, rect):
        r = pygame.draw.rect(surface, random.choice(GameParams.PALETTE), rect)
        r = pygame.draw.rect(surface, (0, 0, 0), rect, 1)
        return r


class BlocksGenerator:
    @staticmethod
    def generate(pattern: list) -> list:
        lst = [Rect(j * GameParams.PIXEL_SIZE,
                    i * GameParams.PIXEL_SIZE,
                    GameParams.PIXEL_SIZE,
                    GameParams.PIXEL_SIZE)
               for j in range(len(pattern[0]))
               for i in range(len(pattern)) if pattern[i][j] == 1]

        return lst


class FigureParser:
    @staticmethod
    def parse() -> dict:
        with open(GameParams.TEMPLATE_PATH) as json_file:
            data = json.load(json_file)

        return data["members"]


def pick_random_figure() -> dict:
    figures = FigureParser.parse()
    return random.choice(figures)


def move_figure(lst: list, key) -> None:
    v = directions[key]
    for block in lst:
        block.move_ip(v)


def move_figure_merged(fig, key) -> None:
    v = directions[key]
    fig.move_ip(v)


def get_merged_tiles(lst: list):
    return reduce(lambda a, b: a.union(b), lst)


def rotate_figure(lst: list, angle: int):
    center = get_merged_tiles(lst).center
    for el in lst:
        res = rotate_point(center[0], center[1], angle, el.topleft)
        el.topleft = res


def rotate_point(cx, cy, angle, p) -> tuple:
    s = math.sin(angle)
    c = math.cos(angle)
    normal_x = p[0] - cx
    normal_y = p[1] - cy
    xnew = normal_x * c - normal_y * s
    ynew = normal_x * s + normal_y * c
    return xnew + cx, ynew + cy
