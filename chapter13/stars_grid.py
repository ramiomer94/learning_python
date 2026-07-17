import pygame
import sys
from star import Star

class StarsGrid() :
    """A class to represent a stars grid."""
    def __init__ (self) :
        """Inititalize the screen surface, stars attributes and a star grid."""
        super().__init__()

        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.screen = pygame.display.set_mode((self.screen_width,
             self.screen_height))
        pygame.display.set_caption('Stars Grid')

        self.stars = pygame.sprite.Group()
        self._create_grid()

        
    def run_grid(self) :
        """
        A loop to display stars grid on the screen and respond to user inputs.
        """
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)
            pygame.display.flip()

            self.clock.tick(60)
    
    def _create_star(self, x_position, y_position) :
        """Create a star object and initialize its position."""
        star = Star(self)
        star.rect.x = x_position
        star.rect.y = y_position
        self.stars.add(star)

    def _create_grid(self) :
        """create multiple rows of stars."""
        star = Star(self)
        star_width, star_height = star.rect.size
        
        current_x = star.rect.x
        current_y = star.rect.y
        while current_y < (self.screen_height - star_height) :
            while current_x < (self.screen_width - star_width) :
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            
            current_x = star_width
            current_y += 2 * star_height


if __name__ == '__main__' :
    sg = StarsGrid()
    sg.run_grid()
    

