import brick
import pygame, sys
from pygame.locals import*

# self.GREEN = (0, 102, 71)
# self.RED = (255, 0, 0)
# self.BLUE = (0, 0, 255)
# self.GOLD = (255, 209, 63)
# self.PURPLE = (255, 0, 255)

pygame.init()
main_surface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Brick pyramid")

bricks = 