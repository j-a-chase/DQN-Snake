################################################################################
# Author: James A. Chase
# Date: 2026-10-28
# File: game_object.py
# Description: Represents a generic game object in the AI Snake game.
################################################################################

# imports
from typing import Protocol

import pygame

class GameObject(Protocol):
    """
    Represents a generic game object in the AI Snake game.
    """
    size: int

    def move(self) -> None:
        """
        Moves the game object.
        """
        ...

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draws the game object on the screen.
        """
        ...

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
