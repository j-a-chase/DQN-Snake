################################################################################
# Author: James A. Chase
# Date: 2026-10-28
# File: snake.py
# Description: Represents the snake object in the AI Snake game.
################################################################################

# imports
from ..helpers import draw_square

from .coordinate import Coordinate
from .game_object import GameObject

from typing import Final

import pygame

Color = tuple[int, int, int]

GREEN: Final[Color] = (0, 255, 0)

class Snake(GameObject):
    """
    Represents the snake object in the AI Snake game.
    """
    def __init__(
            self: Snake,
            start_pos: Coordinate,
            direction: tuple[int, int],
            size: int = 50
        ) -> None:
        """
        Initializer for the Snake class.
        """
        self.size = size
        self._body = [start_pos]
        self._direction = direction

    def move(self: Snake) -> None:
        """
        Moves the snake in the current direction.
        """
        new_head = self._body[0].translate(self._direction[0], self._direction[1])
        self._body = [new_head] + self._body[:-1]

    def draw(self: Snake, surface: pygame.Surface) -> None:
        """
        Draws the snake on the given surface.

        :param surface: The Pygame surface on which to draw the snake.
        :type surface: pygame.Surface
        """
        for segment in self._body:
            draw_square(surface, GREEN, segment.x * self.size, segment.y * self.size, self.size)

    def get_body(self: Snake) -> list[Coordinate]:
        """
        Returns the body of the snake as a list of Coordinate instances.

        :return: A list of Coordinate instances representing the snake's body.
        :rtype: list[Coordinate]
        """
        return self._body

    def set_direction(self: Snake, direction: tuple[int, int]) -> None:
        """
        Sets the direction of the snake.

        :param direction: The new direction for the snake.
        :type direction: tuple[int, int]
        """
        self._direction = direction

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
