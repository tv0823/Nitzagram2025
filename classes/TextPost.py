from classes.Post import *
from helpers import from_text_to_array, center_text


class TextPost(Post):
    def __init__(self, username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        post_display = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, post_display)

        font = pygame.font.SysFont("chalkduster.ttf", TEXT_POST_FONT_SIZE)
        text_arr = from_text_to_array(self.text)

        row_num = 0
        for line in text_arr:
            text = font.render(line, True, self.text_color)
            screen.blit(text, center_text(len(text_arr), text, row_num))
            row_num += 1

        super().display()
