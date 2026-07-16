import pygame

from pygame.sprite import Sprite

class Bullet(Sprite) :
    """
    A class to represent a projectile moving horizantally across the screen.
    """
    def __init__ (self, sws_game) :
        """Initialize the projectile attributes."""
        super().__init__()
        self.settings = sws_game.settings
        self.screen = sws_game.screen
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)
        
        self.rect.midright = sws_game.ship.rect.midright
        self.x = float(self.rect.x)
    
    def update(self) :
        """ Move the bullet up the screen. """
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    
    def draw_bullet(self) :
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


        

