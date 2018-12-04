import pygame, sys
from pygame.locals import*
import logo


pygame.init()
main_surface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Sandy Spring Friends School")


ssfs = logo.Logo(main_surface)
ssfs.draw_rectangles()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
