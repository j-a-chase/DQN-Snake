################################################################################
# Author: James A. Chase
# Date: 2026-11-18
# File: constants.py
# Description: Configurable constants for the Engine
################################################################################

# imports
from typing import Final

import pygame

# colors
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
GRASS: Final[tuple[int, int, int]] = (64, 128, 128)

# rendering
WIN_SIZE: Final[int] = 900
OFFSET: Final[int] = 50
LW: Final[int] = 3  # Line width for the boundaries of the game area

# logic
RENDER_FPS: Final[int] = 120
MOVE_MS: Final[int] = 100 # ten cells per second (matches previous move speed)
GRID_SIZE: Final[int] = 20

GAME_OVER_EVENT: Final[int] = pygame.USEREVENT + 1

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
