import pygame.image

from Post import *
class ImagePost(Post):
    def __init__(self, username, location, description, likes_counter, comments, image):
        super().__init__(username, location, description, likes_counter, comments)
        self.image = image

    def display(self):
        super().display()
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))