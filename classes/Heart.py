import pygame
from constants import *
from helpers import screen
import random

class Heart:
    def __init__(self):
        heart_img = pygame.image.load("Images/Heart.png")
        self.heart_img = pygame.transform.scale(heart_img, (LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT))
        self.heart_pos = (random.randint(0, int(WINDOW_WIDTH - LIKE_BUTTON_WIDTH)), WINDOW_HEIGHT)
        self.speed = 2

    def move(self):
        if(self.heart_pos[1] > 0):
            self.heart_pos = (self.heart_pos[0], self.heart_pos[1] - 2)
            screen.blit(self.heart_img, self.heart_pos)
            screen.blit(self.heart_img, self.heart_pos)
