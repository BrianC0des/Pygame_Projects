import pygame # type: ignore

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
pygame.display.set_caption('Space Ship Game')

while running: 
    #event lool
    for event in  pygame.event.get():
       if event.type == pygame.QUIT:
        running = False

    #draw a game
    display_surface.fill('blue')
    pygame.display.update()



pygame.quit()