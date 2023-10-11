
import sys
import pygame

from code.back.game import Game
from code.front.board import Board
from code.front.constant import DISPLAY_WIDTH, DISPLAY_HEIGHT, BOARD_X, BOARD_Y, BOARD_SIZE


class Interface:

    def __init__(self):
        self.width = DISPLAY_WIDTH
        self.height = DISPLAY_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, (10, 70, 30), (0,  0, self.width, self.height))
