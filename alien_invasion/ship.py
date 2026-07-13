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
        self.settings = ai_game.settings

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

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        


    
    def update(self) :
        """Update the ship's position based on the movement flag."""

        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed
        

        # Note: Yes, rect.x truncates it back down to an integer at that 
        # point — but that's fine, because the next frame's math still starts
        # from the accurate float self.x, not the truncated integer. 
        # The truncation only affects what's drawn on screen for that one 
        # frame, not the ongoing accumulation.
        # In short: self.x is the "true" precise position tracked in the
        # background; self.rect.x is the "display" position pygame actually
        # uses to draw and check collisions. You need to sync them every frame
        # or the two would drift apart and the ship simply wouldn't move.

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self) :
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

