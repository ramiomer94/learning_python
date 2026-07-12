import sys
import pygame

bg_sky_blue = (135, 206, 235)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blue Sky")

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
    
    screen.fill(bg_sky_blue)
    pygame.display.flip()