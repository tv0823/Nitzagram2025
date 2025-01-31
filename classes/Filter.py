import pygame
from constants import *
from helpers import screen

class Filter:
    def __init__(self, color, clear_level):
        self.color = color
        self.clear_level = clear_level

    def apply_filter(self):
        filter_surface = pygame.Surface((POST_WIDTH, POST_HEIGHT), pygame.SRCALPHA)
        filter_surface.fill((*self.color, self.clear_level))
        screen.blit(filter_surface, (POST_X_POS, POST_Y_POS))

