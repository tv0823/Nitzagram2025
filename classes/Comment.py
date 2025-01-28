from helpers import *
import pygame

class Comment:
    def __init__(self,comment_text):
        self.comment_text = comment_text

    def display(self,index):
        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)

        text = font.render(self.comment_text, True, LIGHT_GRAY)
        screen.blit(text,(FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + index * COMMENT_LINE_HEIGHT))