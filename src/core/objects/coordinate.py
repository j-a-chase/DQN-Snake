################################################################################
# Author: James A. Chase
# Date: 2026-10-28
# File: coordinate.py
# Description: Represents a coordinate in the AI Snake game.
################################################################################

# imports
from ..helpers import GRID_SIZE

from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    """
    Represents a coordinate in the AI Snake game.
    """
    x: int
    y: int

    def translate(self: Coordinate, dx: int = 0, dy: int = 0) -> Coordinate:
        """
        Returns a new Coordinate instance with the specified translation
        applied.

        :param dx: The horizontal translation to apply.
        :type dx: int
        :param dy: The vertical translation to apply.
        :type dy: int
        :return: A new Coordinate instance with the translation applied.
        :rtype: Coordinate
        """
        return Coordinate(self.x + dx, self.y + dy)

    def validate(self: Coordinate) -> bool:
        if 0 <= self.x < GRID_SIZE and 0 <= self.y < GRID_SIZE:
            return True
        return False

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
