import Post
from helpers import *
import pygame
class Comment:
    def _init_(self,comment_text):
        self.comment_text = comment_text

    def display(self,index):
        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)

        text = font.render(self.comment_text, True, BLACK)
        screen.blit(text,(FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS * index))