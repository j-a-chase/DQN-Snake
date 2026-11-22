################################################################################
# Author: James A. Chase
# Date: 2026-10-28
# File: graphics.py
# Description: Graphics helper functions using Pygame.
################################################################################

# imports
from .colors import Colors

import pygame

def draw_rect(surface: pygame.Surface, color: Colors, x: int, y: int, width: int, height: int) -> None:
    """
    Draws a rectangle on the given Pygame surface.

    :param surface: The Pygame surface on which to draw the rectangle.
    :type surface: pygame.Surface
    :param color: The color of the rectangle.
    :type color: Color
    :param x: The x-coordinate of the top-left corner of the rectangle.
    :type x: int
    :param y: The y-coordinate of the top-left corner of the rectangle.
    :type y: int
    :param width: The width of the rectangle.
    :type width: int
    :param height: The height of the rectangle.
    :type height: int
    """
    pygame.draw.rect(surface, color.value, (x, y, width, height))

def draw_square(surface: pygame.Surface, color: Colors, x: int, y: int, size: int) -> None:
    """
    Draws a square on the given Pygame surface.

    :param surface: The Pygame surface on which to draw the square.
    :type surface: pygame.Surface
    :param color: The color of the square.
    :type color: Color
    :param x: The x-coordinate of the top-left corner of the square.
    :type x: int
    :param y: The y-coordinate of the top-left corner of the square.
    :type y: int
    :param size: The size of the square.
    :type size: int
    """
    draw_rect(surface, color, x, y, size, size)

def draw_game_box(
        surface: pygame.Surface,
        color: Colors,
        offset: int,
        size: int,
        width: int
    ) -> None:
    """
    Draws the box that contains all of the game objects.

    :param surface: The Pygame surface on which to draw the game box.
    :type surface: pygame.Surface
    :param color: The color of the game box.
    :type color: Color
    :param offset: The offset of the game box from the top-left corner.
    :type offset: int
    :param size: The size of the game box.
    :type size: int
    :param width: The width of the game box.
    :type width: int
    """
    draw_rect(surface, color, offset, offset, size - 2 * offset, width)  # top
    draw_rect(
        surface, color, offset, size - offset - width, size - 2 * offset, width
    )  # bottom
    draw_rect(surface, color, offset, offset, width, size - 2 * offset)  # left
    draw_rect(
        surface, color, size - offset - width, offset, width, size - 2 * offset
    )  # right

def draw_button(
        screen: pygame.Surface, font: pygame.Font, btn: pygame.Rect,
        txt: str, mouse_pos: tuple[int, int]
    ) -> None:
    """
    Draws a menu button on the screen.

    :param screen: The Pygame surface to draw the button on.
    :type screen: pygame.Surface
    :param font: The font used to render the Button text
    :type font: pygame.Font
    :param btn: The button rectangle object to draw.
    :type btn: pygame.Rect
    :param txt: The text to render on the button.
    :type txt: str
    :param mouse_pos: A tuple containing the x and y coordinates of the mouse
    :type mouse_pos: tuple[int, int]
    """
    color = Colors.HOVER if btn.collidepoint(mouse_pos) else Colors.BTN
    pygame.draw.rect(screen, color.value, btn, border_radius=8)

    btn_text = font.render(txt, True, Colors.BG_COLOR.value)
    screen.blit(btn_text, btn_text.get_rect(center=btn.center))

if __name__ == '__main__':
    assert False, "This file is not intended to be run directly."
