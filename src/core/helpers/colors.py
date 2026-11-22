################################################################################
# Author: James A. Chase
# Date: 2026-11-21
# File: colors.py
# Description: 
################################################################################

# imports
from enum import Enum

class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SNAKE = (0, 255, 0)
    FOOD = (128, 128, 0)
    GRASS = (64, 128, 128)
    BTN   = (60, 60, 60)
    HOVER = (128, 128, 128)

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
