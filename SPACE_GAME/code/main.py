import pygame # type: ignore
from os.path import join
import random



WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

#plain surface
surf = pygame.Surface((100, 200))
surf.fill('red')
x = 100
y = 150

#importing image 

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()

while running: 
    #event lool
    for event in  pygame.event.get():
       if event.type == pygame.QUIT:
        running = False

    #draw a game
    display_surface.fill('darkgray')
    x += 0.1
    display_surface.blit(player_surf, (x, y))
    pygame.display.update()



pygame.quit()