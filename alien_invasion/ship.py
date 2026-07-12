import pygame

class Ship :
    """ A class to manage the ship. """
    def __init__ (self, ai_game) :
        """Initialize the ship and set its starting position."""

        # Pygame is efficient because it lets you treat all game elements like
        # rectangles (rects), even if they’re not exactly shaped like
        # rectangles. Treating an element as a rectangle is efficient because
        # rectangles are simple geometric shapes. When Pygame needs to figure
        # out whether two game elements have collided, for example, it can do
        # this more quickly if it treats each object as a rectangle. 

        # We then assign the screen to an attribute of Ship 1, so we can
        # access it easily in all the methods in this class. 
        self.screen = ai_game.screen

        # We access the screen’s rect attribute using the get_rect() method and
        # assign it to self.screen_rect 2. Doing so allows us to place the ship
        # in the correct location on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        # To load the image, we call pygame.image.load() 3 and give it the
        # location of our ship image. This function returns a surface 
        # representing the ship, which we assign to self.image. 
        self.image = pygame.image.load('images/ship.bmp')

        # we call get_rect() to access the ship surface’s rect attribute so
        # we can later use it to place the ship.
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
    
    def update(self) :
        """Update the ship's position based on the movement flag."""
        if self.moving_right :
            self.rect.x += 1
        if self.moving_left :
            self.rect.x -= 1

    def blitme(self) :
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

