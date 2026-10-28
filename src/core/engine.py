################################################################################
# Author: James A. Chase
# Date: 2026-10-27
# File: engine.py
# Description: Core engine for the AI Snake game, handling game logic, updates,
#              and rendering.
################################################################################

# imports
import pygame

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

        pygame.init()
        self._screen = pygame.display.set_mode((800, 600))  # Set up the game window
        pygame.display.set_caption("DQN Snake")  # Set the window title
        self._clock = pygame.time.Clock()  # Create a clock object to control the game speed
        self._fps = 60  # Set the desired frames per second for the game

    def run(self: Engine) -> None:
        """
        Runs the main game loop, handling updates and rendering.
        """
        while self._running:
            self._update()
            self._render()
            self._clock.tick(self._fps)  # Control the game speed based on the desired FPS

    def _update(self: Engine) -> None:
        """
        Updates the game state.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def _render(self: Engine) -> None:
        """
        Renders the game.
        """
        self._screen.fill((0, 0, 0))  # Clear the screen with black
        pygame.display.flip()  # Update the display with the rendered frame

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
