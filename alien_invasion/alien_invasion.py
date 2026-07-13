# We’ll use tools in the sys module to exit the game when the player quits.
import sys  
# The pygame module contains the functionality we need to make a game. 
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    def __init__(self):
        """Initialize the game, and create game resources."""

        # the pygame.init() function initializes the background settings that
        # Pygame needs to work properly 
        pygame.init()

        # create an instance of the class Clock, from the pygame.time module. 
        self.clock = pygame.time.Clock()

        # create an instance of the Settings class that is assigned to settings
        # the setting instance stores screen settings and ship settings
        self.settings = Settings() 
        
        # we call pygame.display.set_mode() to create a display window 2,
        #  on which we’ll draw all the game’s graphical elements.

        # The argument (1200, 800) is a tuple that defines the dimensions
        # of the game window, which will be 1,200 pixels wide by 800 pixels
        #  high. (You can adjust these values depending on your display size.)
        # self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width, self.settings.screen_height))

        # To run the game in fullscreen mode, make the following changes in
        # __init__():
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height 

        # If you like how the game looks or behaves in fullscreen mode, keep
        # these settings. If you liked the game better in its own window, you
        # can revert back to the original approach where we set a specific 
        # screen size for the game.

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)




    # The game is controlled by the run_game() method. This method contains 
    # a while loop that runs continually. The while loop contains an event
    # loop and code that manages screen updates.
    def run_game(self) :
        """ Start the main loop for the game."""
        while True :
            # Watch for keyboard and mouse events.
            self._check_events()

            # The ship’s position will be updated after we’ve checked for
            # keyboard events and before we update the screen. This allows
            # the ship’s position to be updated in response to player input
            # and ensures the updated position will be used when drawing the
            # ship to the screen
            self.ship.update()
            # Redraw the screen during each pass through the loop.
            self._update_screen()

            # The tick() method takes one argument: the frame rate for the
            # game. Here I’m using a value of 60, so Pygame will do its best
            # to make the loop run exactly 60 times per second.
            self.clock.tick(60)
    
    def _check_events(self) :
        """Respond to keypresses and mouse events."""

        # An event is an action that the user performs while playing the
        # game, such as pressing a key or moving the mouse. To make our
        # program respond to events, we write an event loop to listen for
        # events and perform appropriate tasks depending on the kinds of
        # events that occur. The for loop 4 nested inside the while loop
        # is an event loop
        for event in pygame.event.get() :
            #  Inside the loop, we’ll write a series of if statements to
            #  detect and respond to specific events. For example,
            #  when the player clicks the game window’s close button,
            #  a pygame.QUIT event is detected and we call sys.exit()
            #  to exit the game 
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP :
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) :
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT :
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT :
            self.ship.moving_left = True
        elif event.key == pygame.K_q :
            sys.exit()
    
    def _check_keyup_events(self, event) :
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT :
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT :
            self.ship.moving_left = False
            
    
    def _update_screen(self) :
        """Update images on the screen, and flip to the new screen."""

        # We fill the screen with the background color using the fill()
        # method 2, which acts on a surface and takes only one argument:
        # a color.
        self.screen.fill(self.settings.bg_color)

        # To draw the player’s ship on the screen, we’ll load an image and
        # then use the Pygame blit() method to draw the image.
        self.ship.blitme()

        # The call to pygame.display.flip() tells Pygame to make the most
        # recently drawn screen visible.
        pygame.display.flip()

    

# At the end of the file, we create an instance of the game and then call
# run_game(). We place run_game() in an if block that only runs if the file is
# called directly. When you run this alien_invasion.py file, you should see an
# empty Pygame window.
if __name__ == '__main__' :
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


    
