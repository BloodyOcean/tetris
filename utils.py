import random

from TemplateParser import FigureParser


def pick_random_figure() -> dict:
    figures = FigureParser.parse()
    return random.choice(figures)
