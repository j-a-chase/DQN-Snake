################################################################################
# Author: James A. Chase
# Date: 2026-10-28
# File: snake.py
# Description: Represents the snake object in the AI Snake game.
################################################################################

# imports
from ..helpers import Colors, draw_square, GAME_OVER_EVENT, OFFSET

from .coordinate import Coordinate
from .game_object import GameObject

import pygame

class Snake(GameObject):
    """
    Represents the snake object in the AI Snake game.
    """
    def __init__(
            self: Snake,
            start_pos: Coordinate,
            direction: tuple[int, int],
            size: int = 40
        ) -> None:
        """
        Initializer for the Snake class.
        """
        self.size = size
        self._body = [start_pos]
        self._previous_body = self._body.copy()
        self._interpolation = 1.0
        self._direction = direction

    def move(self: Snake) -> None:
        """
        Moves the snake in the current direction.
        """
        self._previous_body = self._body.copy()
        new_head = self.head().translate(self._direction[0], self._direction[1])
        if not new_head.validate():
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))
            return
        self._body = [new_head] + self._body[:-1]

    def draw(self: Snake, surface: pygame.Surface) -> None:
        """
        Draws the snake on the given surface.

        :param surface: The Pygame surface on which to draw the snake.
        :type surface: pygame.Surface
        """
        for idx, segment in enumerate(self._body):
            previous = self._previous_body[idx]
            x = round(
                OFFSET
                + (previous.x + (segment.x - previous.x) * self._interpolation - 1)
                * self.size
            )
            y = round(
                OFFSET
                + (previous.y + (segment.y - previous.y) * self._interpolation - 1)
                * self.size
            )
            draw_square(surface, Colors.SNAKE, x, y, self.size)

    def head(self: Snake) -> Coordinate:
        """
        Returns the body of the snake as a list of Coordinate instances.

        :return: A list of Coordinate instances representing the snake's body.
        :rtype: list[Coordinate]
        """
        return self._body[0]

    def extend(self: Snake) -> None:
        """
        Extends the Snake by one segment.
        """
        tail = self._previous_body[-1]
        self._body.append(tail)
        self._previous_body.append(tail)

    def set_direction(self: Snake, direction: tuple[int, int]) -> None:
        """
        Sets the direction of the snake.

        :param direction: The new direction for the snake.
        :type direction: tuple[int, int]
        """
        self._direction = direction

    def set_interpolation(self: Snake, alpha: float) -> None:
        """
        Sets the interpolation factor for the snake's rendering.

        :param alpha: The new interpolation value
        :type alpha: float
        """
        self._interpolation = alpha

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
