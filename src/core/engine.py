################################################################################
# Author: James A. Chase
# Date: 2026-10-27
# File: engine.py
# Description: Core engine for the AI Snake game, handling game logic, updates,
#              and rendering.
################################################################################

# imports
from .helpers import (
    Colors, draw_square, draw_game_box, draw_button, WIN_SIZE, OFFSET, LW,
    RENDER_FPS, GAME_OVER_EVENT, GAME_SPEED, State
)
from .objects import Snake, Coordinate, Food
from .dataclasses import Configuration

from pathlib import Path
import pygame
import json

class Engine:
    """
    Core engine class for the AI Snake game.
    Handles game logic, updates, and rendering.
    """
    def __init__(
            self: Engine,
            snake_pos: Coordinate = Coordinate(5, 5),
            food_pos: Coordinate = Coordinate(8, 8)
        ) -> None:
        """
        Initializer for the Engine class.

        :param snake_pos: Starting position for the snake
        :type snake_pos: Coordinate
        :param food_pos: Starting position for the food
        :type food_pos: Coordinate
        """
        self.state: State = State.START
        self._score = 0  # Initialize the score to 0
        self._move_ms = 100
        self._config = Configuration()

        pygame.init()
        pygame.display.set_caption("DQN Snake")  # Set the window title
        
        self._screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))  # Set up the game window
        self._clock = pygame.Clock()  # Create a clock object to control the game speed

        self._snake = Snake(snake_pos, (1, 0))
        self._food = Food(food_pos)

    def run(self: Engine) -> None:
        """
        Runs the main game loop, handling updates and rendering.
        """
        self._load_config()

        if self._config.difficulty != "normal":
            self._move_ms = GAME_SPEED[self._config.difficulty]

        # (x, y, width, height)
        self._play_btn = pygame.Rect(350, 220, 200, 60)
        self._quit_btn = pygame.Rect(350, 310, 200, 60)

        accumulator: float = 0.0
        while True:
            self._update()
            tick = self._clock.tick(RENDER_FPS)
            if self.state == State.EXIT:
                return
            
            if self.state == State.RUNNING:
                accumulator += tick
                while accumulator >= self._move_ms:
                    self._snake.move()
                    accumulator -= self._move_ms
                    if self._snake.head() == self._food.pos:
                        self._score += 100
                        self._snake.extend()
                        self._food.move()
                    if len(self._snake.body) > 1 and self._snake.head() in self._snake.body[1:]:
                        self.state = State.GAME_OVER
                        break

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
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = State.EXIT
                return
            
            if event.type == GAME_OVER_EVENT:
                self.state = State.GAME_OVER
                return

            if self.state == State.GAME_OVER and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = State.EXIT
                    return
                if event.key == pygame.K_r:
                    self.state = State.START
                    self._snake = Snake(Coordinate(5, 5), (1, 0))
                    self._food = Food(Coordinate(8, 8))
                    self._score = 0

            if self.state == State.MENU and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    if self._play_btn.collidepoint(mouse_pos):
                        self.state = State.RUNNING
                    elif self._quit_btn.collidepoint(mouse_pos):
                        self.state = State.EXIT
                        return

            if self.state == State.RUNNING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = State.MENU
                    if event.key == pygame.K_DOWN:
                        self._snake.set_direction((0, 1))
                    if event.key == pygame.K_UP:
                        self._snake.set_direction((0, -1))
                    if event.key == pygame.K_RIGHT:
                        self._snake.set_direction((1, 0))
                    if event.key == pygame.K_LEFT:
                        self._snake.set_direction((-1, 0))

            if self.state == State.START and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = State.EXIT
                    return
                if event.key == pygame.K_SPACE:
                    self.state = State.RUNNING

    def _render(self: Engine) -> None:
        """
        Renders the game.
        """
        self._screen.fill(Colors.BG_COLOR.value)

        # Draw the Game Title at the top of the screen, left aligned, offset
        font = pygame.font.SysFont("Segoe UI Semibold", 40)
        title_text = font.render("DQN Snake", True, Colors.TXT_COLOR.value)
        self._screen.blit(title_text, (OFFSET, 0))

        # Draw the score opposite the title with offset
        score_text = font.render(f"Score: {self._score}", True, Colors.TXT_COLOR.value)
        self._screen.blit(score_text, (WIN_SIZE - score_text.get_width() - OFFSET, 0))

        if self.state in [ State.RUNNING, State.GAME_OVER ]:
            # Draw the background and static elements of the game area (grass field)
            draw_square(
                self._screen,
                Colors.GRASS,
                OFFSET + LW,
                OFFSET + LW,
                WIN_SIZE - 2 * OFFSET - 2 * LW
            )

            # Draw game objects
            self._snake.draw(self._screen)
            self._food.draw(self._screen)

            # Draw the boundaries of the game area (over the snake if it collides)
            draw_game_box(self._screen, Colors.TXT_COLOR, OFFSET, WIN_SIZE, LW)

            # draw game over text over the ending game state
            if self.state == State.GAME_OVER:
                msg = font.render((txt := "Game Over! Press 'R' to restart!"), True, Colors.TXT_COLOR.value)
                msg_w = WIN_SIZE - len(txt)
                self._screen.blit(msg, msg.get_rect(center=(msg_w / 2, 300)))
        elif self.state == State.START:
            msg = font.render((txt := "Press SPACE to play!"), True, Colors.TXT_COLOR.value)
            msg_w = WIN_SIZE - len(txt)
            self._screen.blit(msg, msg.get_rect(center=(msg_w / 2, 300)))
        elif self.state == State.MENU:
            mouse_pos = pygame.mouse.get_pos()
            draw_button(self._screen, font, self._play_btn, "Play", mouse_pos)
            draw_button(self._screen, font, self._quit_btn, "Quit", mouse_pos)

        pygame.display.flip()  # Update the display with the rendered frame

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
