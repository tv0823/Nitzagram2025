import pygame.image
from classes.Post import *

class ImagePost(Post):
    def __init__(self, username, location, description, image):
        super().__init__(username, location, description)
        self.image = image

    def display(self):
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))
        super().display()