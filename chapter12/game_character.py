import sys
import pygame



SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
background_color = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption('AC Black Flag Edward Kenway')

character_image = pygame.image.load('EdwardKenway.bmp')
character_rect = character_image.get_rect()
character_rect.center = screen_rect.center


while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
    
    screen.fill(background_color)
    screen.blit(character_image, character_rect)
    pygame.display.flip()



