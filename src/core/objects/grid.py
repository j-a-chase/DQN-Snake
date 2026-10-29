################################################################################
# Author: James A. Chase
# Date: 2026-10-28
# File: grid.py
# Description: The internal representation of the grid in the AI Snake game.
################################################################################

# imports
from .coordinate import Coordinate
from .game_object import GameObject

from typing import Optional

class Grid:
    """
    Represents the grid in the AI Snake game.
    """
    def __init__(self: Grid, width: int = 20, height: int = 20) -> None:
        """
        Initializer for the Grid class.

        :param width: The width of the grid.
        :type width: int
        :param height: The height of the grid.
        :type height: int
        """
        self._width = width
        self._height = height
        self._cells: list[Optional[GameObject]] = [None] * (width * height)

    def get_cell(self, coordinate: Coordinate) -> Optional[GameObject]:
        """
        Retrieves the game object at the specified coordinate.

        :param coordinate: The coordinate of the cell to retrieve.
        :type coordinate: Coordinate
        :return: The game object at the specified coordinate, or None if the cell is empty.
        :rtype: Optional[GameObject]
        """
        index = coordinate.y * self._width + coordinate.x
        return self._cells[index]

    def set_cell(self, coordinate: Coordinate, game_object: Optional[GameObject]) -> None:
        """
        Sets the game object at the specified coordinate.

        :param coordinate: The coordinate of the cell to set.
        :type coordinate: Coordinate
        :param game_object: The game object to place at the specified coordinate, or None to clear the cell.
        :type game_object: Optional[GameObject]
        """
        index = coordinate.y * self._width + coordinate.x
        self._cells[index] = game_object

    def clear_cell(self, coordinate: Coordinate) -> None:
        """
        Clears the game object at the specified coordinate.

        :param coordinate: The coordinate of the cell to clear.
        :type coordinate: Coordinate
        """
        self.set_cell(coordinate, None)

    def clear_grid(self) -> None:
        """
        Clears all cells in the grid.
        """
        self._cells = [None] * (self._width * self._height)

    def is_cell_empty(self, coordinate: Coordinate) -> bool:
        """
        Checks if the cell at the specified coordinate is empty.

        :param coordinate: The coordinate of the cell to check.
        :type coordinate: Coordinate
        :return: True if the cell is empty, False otherwise.
        :rtype: bool
        """
        return self.get_cell(coordinate) is None

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
