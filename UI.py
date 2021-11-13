import pygame as pg  # as constructor arg?
from typing import Tuple

RGB_COLOUR = Tuple[int, int, int]


class Display:
    def __init__(self):
        # display
        self._SIZE = self.WIDTH, self.HEIGHT = 512, 512  # width, height
        self._DIMENSION: int = 8  # dimension
        self._SQ_SIZE: int = int(self.HEIGHT / self._DIMENSION)
        self._display = pg.display.set_mode(self._SIZE)

    def draw(self):
        self._draw_board()
        self._update()

    def _draw_board(self):
        colors: Tuple[RGB_COLOUR, RGB_COLOUR] = ((70, 38, 0), (190, 153, 102))
        for file in range(self._DIMENSION):
            for row in range(self._DIMENSION):
                color = colors[((file + row) % 2)]
                self._draw_square((file, row), color)

    @staticmethod
    def _update():
        """
        update the screen
        """
        pg.display.update()

    def _draw_square(self, pos: Tuple[int, int], color: RGB_COLOUR):
        """
        draw a square on the screen
        :param pos: position of the square
        :param color: color of the square
        """
        size = self._SQ_SIZE
        x, y = pos
        pg.draw.rect(self._display, color, pg.Rect(x * size, y * size, size, size))

