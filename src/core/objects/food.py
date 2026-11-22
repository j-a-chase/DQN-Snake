################################################################################
# Author: James A. Chase
# Date: 2026-10-28
# File: food.py
# Description: Represents the food object in the game.
################################################################################

# imports
from ..helpers import Colors, GRID_SIZE, OFFSET, draw_square

from .coordinate import Coordinate
from .game_object import GameObject

import random
import pygame

# code
class Food(GameObject):
    """
    Represents the food object in the game.
    """
    def __init__(
            self, position: Coordinate, size: int = 40
        ) -> None:
        """
        Constructor

        :param position: The position for the Food
        :type position: Coordinate
        :param size: The size used to render the Food
        :type size: int
        """
        self.size = size
        self.pos = position

    def move(self: Food) -> None:
        """
        Moves the food object to a random position on the grid.
        """
        self.pos = Coordinate(
            random.randint(1, GRID_SIZE),
            random.randint(1, GRID_SIZE)
        )
        assert self.pos.validate(), f"Position - {self.pos}"

    def draw(self: Food, surface: pygame.Surface) -> None:
        """
        Draws the food at its stored position.

        :param surface: The surface for the food to draw on.
        :type surface: pygame.Surface
        """
        x = OFFSET + (self.pos.x - 1) * self.size
        y = OFFSET + (self.pos.y - 1) * self.size
        draw_square(surface, Colors.FOOD, x, y, self.size)

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
