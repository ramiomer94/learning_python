import pygame
import sys

class Keys :
    """A class to create an empty screen and print key events"""
    def __init__ (self) :
        """Initialize the screen and its settings"""
        pygame.init()

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250, 250, 250)
        
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption('Keys')

    def run_event_loop(self) :
        """
        Run the event loop to print the event.key attribute 
        whenever a pygame.KEYDOWN event is detected.
        """
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    sys.exit()
                elif event.type == pygame.KEYDOWN :
                    print(pygame.key.name(event.key))
            
            self.screen.fill(self.bg_color)
            pygame.display.flip()

keys = Keys()
keys.run_event_loop()
