import pygame # type: ignore

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True


surf = pygame.Surface((100, 200))
surf.fill('red')
x = 100
y = 150

while running: 
    #event lool
    for event in  pygame.event.get():
       if event.type == pygame.QUIT:
        running = False

    #draw a game
    display_surface.fill('darkgray')
    x += 2
    display_surface.blit(surf, (x, y))
    pygame.display.update()



pygame.quit()