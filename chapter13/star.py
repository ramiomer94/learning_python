import pygame
from pygame.sprite import Sprite

class Star(Sprite) :
    """A class representing a start."""
    def __init__ (self, start_grid) :
        """Initialize star attributes and the initial position of a star."""
        super().__init__()

        self.screen = start_grid.screen

        self.image = pygame.image.load('images/starman.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    

