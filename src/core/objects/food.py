################################################################################
# Author: James A. Chase
# Date: 2026-10-28
# File: food.py
# Description: Represents the food object in the game.
################################################################################

# imports
from .coordinate import Coordinate
from .game_object import GameObject

import random

# code
class Food(GameObject):
    """
    Represents the food object in the game.
    """
    def __init__(self, coordinate: Coordinate) -> None:
        self._pos = coordinate

    def move(self, grid_width: int, grid_height: int) -> None:
        """
        Moves the food object to a random position on the grid.
        """
        self._pos = Coordinate(
            random.randint(0, grid_width - 1),
            random.randint(0, grid_height - 1)
        )

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
