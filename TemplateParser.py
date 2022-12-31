import json

from GameParameters import GameParams


class FigureParser:
    @staticmethod
    def parse() -> dict:
        with open(GameParams.TEMPLATE_PATH) as json_file:
            data = json.load(json_file)

        return data["members"]
