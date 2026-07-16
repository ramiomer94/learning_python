import pygame
from settings import Settings

class Ship :
    """A class to represent a ship - a game elements that moves up and down """
    def __init__ (self, sws_game) :
        """Initialize the attributes of the ship"""
        self.screen = sws_game.screen
        self.screen_rect = sws_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.moving_up = False
        self.moving_down = False

        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        self.settings = Settings()
    
    def update(self) :
        """Update the position of the ship"""
        if self.moving_up and self.rect.top > 0 :
            self.y -= self.settings.ship_speed
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
            self.y += self.settings.ship_speed
        
        self.rect.y = self.y
    

    def blitme(self) :
        """draw the ship to the screen"""
        self.screen.blit(self.image, self.rect)

