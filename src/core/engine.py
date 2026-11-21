################################################################################
# Author: James A. Chase
# Date: 2026-10-27
# File: engine.py
# Description: Core engine for the AI Snake game, handling game logic, updates,
#              and rendering.
################################################################################

# imports
from .helpers import (
    draw_square, draw_game_box, BLACK, WHITE, GRASS,
    WIN_SIZE, OFFSET, LW, RENDER_FPS, GAME_OVER_EVENT
)
from .objects import Snake, Coordinate
from .dataclasses import Configuration

from pathlib import Path
import pygame
import json

GAME_SPEED: dict[str, int] = {
    "easy": 150,
    "hard": 67
}

class Engine:
    """
    Core engine class for the AI Snake game.
    Handles game logic, updates, and rendering.
    """
    def __init__(
            self: Engine,
            start_pos: Coordinate = Coordinate(5, 5)
        ) -> None:
        """
        Initializer for the Engine class.
        """
        self._running = True
        self._is_game_over = False
        self._score = 0  # Initialize the score to 0
        self._move_ms = 100
        self._config = Configuration()

        pygame.init()
        pygame.display.set_caption("DQN Snake")  # Set the window title
        
        self._screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))  # Set up the game window
        self._clock = pygame.Clock()  # Create a clock object to control the game speed

        self._snake = Snake(start_pos, (1, 0))

    def run(self: Engine) -> None:
        """
        Runs the main game loop, handling updates and rendering.
        """
        self._load_config()

        if self._config.difficulty != "normal":
            self._move_ms = GAME_SPEED[self._config.difficulty]

        accumulator: float = 0.0
        while self._running:
            self._update()
            if not self._is_game_over:
                accumulator += self._clock.tick(RENDER_FPS)

                while accumulator >= self._move_ms:
                    self._snake.move()
                    accumulator -= self._move_ms

                self._snake.set_interpolation(accumulator / self._move_ms)
                self._render()

    def _load_config(self: Engine) -> None:
        """
        Loads the game configuration.
        """
        try:
            with open(Path("config/config.json")) as cf:
                data = json.loads(cf.read())
                self._config.load(data)
        except json.JSONDecodeError:
            print("Error loading configuration data!")
            raise

    def _update(self: Engine) -> None:
        """
        Updates the game state.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == GAME_OVER_EVENT:
                self._is_game_over = True
                print("GAME OVER!")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._running = False
                if event.key == pygame.K_DOWN:
                    self._snake.set_direction((0, 1))
                if event.key == pygame.K_UP:
                    self._snake.set_direction((0, -1))
                if event.key == pygame.K_RIGHT:
                    self._snake.set_direction((1, 0))
                if event.key == pygame.K_LEFT:
                    self._snake.set_direction((-1, 0))

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

        # Draw game objects
        self._snake.draw(self._screen)

        # Draw the boundaries of the game area (over the snake if it collides)
        draw_game_box(self._screen, BLACK, OFFSET, WIN_SIZE, LW)

        pygame.display.flip()  # Update the display with the rendered frame

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
