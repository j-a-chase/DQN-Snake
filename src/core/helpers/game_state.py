################################################################################
# Author: James A. Chase
# Date: 2026-11-21
# File: game_state.py
# Description: 
################################################################################

# imports
from enum import StrEnum, auto

class State(StrEnum):
    START = auto()
    RUNNING = auto()
    MENU = auto()
    GAME_OVER = auto()
    EXIT = auto()

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
