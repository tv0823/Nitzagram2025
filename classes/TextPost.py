from msilib import type_string

import pygame

from Post import *
from helpers import from_text_to_array, center_text


class TextPost(Post):
    def __init__(self, username, location, description, likes_counter, comments, text, text_color, background_color):
        super().__init__(username, location, description, likes_counter, comments)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        post_display = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, post_display)

        font = pygame.font.SysFont("chalkduster.ttf", TEXT_POST_FONT_SIZE)
        text_arr = from_text_to_array(self.text)
        for text in text_arr:
            screen.blit(text, center_text(len(text_arr), text, len(text)))
        super().display()
