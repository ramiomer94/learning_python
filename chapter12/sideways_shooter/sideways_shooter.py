import pygame
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet

class SidewaysShooter :
    """
    A class to represesnt a game of a ship moving up and down and shooting
    bullets horizontally to destroy aliens
    
    """

    def __init__ (self) :
        """Initialize the game, and the game attributes"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Sideways Shooter')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self) :
        """The main loop to run the game and respond to user inputs"""
        while True :
            self._check_event()
            self._update_screen()
            self._update_bullets()
            self.clock.tick(60)

    def _check_event(self) :
        """Respond to the user's keyboard or mouse inputs"""
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()
            if event.type == pygame.KEYDOWN :
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP :
                self._check_keyup_event(event)

    def _check_keydown_event(self,event) :
        """Respond to key presses."""
        if event.key == pygame.K_q :
            sys.exit()
        elif event.key == pygame.K_UP :
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN :
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _check_keyup_event(self, event) :
        """Respond to key releases."""
        if event.key == pygame.K_UP :
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN :
            self.ship.moving_down = False
    
    def _draw_bullets(self) :
        """Draw bullets to the screen"""
        self.bullets.update()
        for bullet in self.bullets.sprites() :
            bullet.draw_bullet()
    
    def _update_bullets(self):
        """
        update the position and delete bullets that disappear off the screen
        """
        self._draw_bullets()
        for bullet in self.bullets.copy() :
            if bullet.rect.left >= self.ship.screen_rect.right :
                self.bullets.remove(bullet)

    
    def _update_screen(self) :
        """Draw the ship to the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self._draw_bullets()
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__' :
    sideways_shooter = SidewaysShooter();
    sideways_shooter.run_game()
