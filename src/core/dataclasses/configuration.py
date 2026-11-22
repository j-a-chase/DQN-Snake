################################################################################
# Author: James A. Chase
# Date: 2026-11-21
# File: configuration.py
# Description: A collection of simple dataclasses for the game.
################################################################################

# imports
from dataclasses import dataclass

@dataclass
class Configuration:
    difficulty: str = "normal"
    theme: str = "light"

    def load(self: Configuration, data: dict):
        self.difficulty = data["difficulty"]
        self.theme = data["theme"]

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
