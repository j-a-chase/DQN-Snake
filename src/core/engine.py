################################################################################
# Author: James A. Chase
# Date: 2026-10-27
# File: engine.py
# Description: Core engine for the AI Snake game, handling game logic, updates,
#              and rendering.
################################################################################

# imports
from .helpers import draw_square, draw_game_box, draw_game_objects
from .objects import Snake, Coordinate, GameObject

from typing import Final, cast

import pygame

# colors for the game
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
GRASS: Final[tuple[int, int, int]] = (64, 128, 128)

# layout constants for the game area
WIN_SIZE: Final[int] = 900
OFFSET: Final[int] = 50
LW: Final[int] = 3  # Line width for the boundaries of the game area

# engine constants
FPS: Final[int] = 10
SNAKE_IDX: Final[int] = 0

class Engine:
    """
    Core engine class for the AI Snake game.
    Handles game logic, updates, and rendering.
    """
    def __init__(self: Engine) -> None:
        """
        Initializer for the Engine class.
        """
        self._running = True
        self._score = 0  # Initialize the score to 0

        pygame.init()
        pygame.display.set_caption("DQN Snake")  # Set the window title
        
        self._screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))  # Set up the game window
        self._clock = pygame.Clock()  # Create a clock object to control the game speed

        self._objs: list[GameObject] = []

    def run(self: Engine) -> None:
        """
        Runs the main game loop, handling updates and rendering.
        """
        self._objs.append(Snake(Coordinate(5, 5), (1, 0)))  # Add a snake object to the game
        while self._running:
            self._update()
            self._render()
            self._clock.tick(FPS)  # Control the game speed based on the desired FPS

    def _update(self: Engine) -> None:
        """
        Updates the game state.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._running = False
                if event.key == pygame.K_DOWN:
                    cast(Snake, self._objs[SNAKE_IDX]).set_direction((0, 1))
                if event.key == pygame.K_UP:
                    cast(Snake, self._objs[SNAKE_IDX]).set_direction((0, -1))
                if event.key == pygame.K_RIGHT:
                    cast(Snake, self._objs[SNAKE_IDX]).set_direction((1, 0))
                if event.key == pygame.K_LEFT:
                    cast(Snake, self._objs[SNAKE_IDX]).set_direction((-1, 0))

        for obj in self._objs:
            obj.move()

    def _render(self: Engine) -> None:
        """
        Renders the game.
        """
        self._screen.fill(WHITE)

        # Draw the Game Title at the top of the screen, left aligned, offset
        font = pygame.font.SysFont("Segoe UI Semibold", 40)
        title_text = font.render("DQN Snake", True, BLACK)
        self._screen.blit(title_text, (OFFSET, 0))

        # Draw the score opposite the title with offset
        score_text = font.render(f"Score: {self._score}", True, BLACK)
        self._screen.blit(score_text, (WIN_SIZE - score_text.get_width() - OFFSET, 0))

        # Draw the background and static elements of the game area (grass field)
        draw_square(
            self._screen,
            GRASS,
            OFFSET + LW,
            OFFSET + LW,
            WIN_SIZE - 2 * OFFSET - 2 * LW
        )

        # Draw the boundaries of the game area
        draw_game_box(self._screen, BLACK, OFFSET, WIN_SIZE, LW)

        # Draw game objects
        draw_game_objects(self._screen, self._objs)

        pygame.display.flip()  # Update the display with the rendered frame

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
