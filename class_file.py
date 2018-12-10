import brick
import pygame, sys
from pygame.locals import*

GREEN = (0, 102, 71)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 209, 63)
PURPLE = (255, 0, 255)
SPACE = 5
HEIGHT = 20
x_number_bricks = 9
colors = [RED, BLUE, GOLD, PURPLE, GREEN]


pygame.init()
main_surface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Brick pyramid")

WIDTH = (500 - (x_number_bricks * SPACE))/x_number_bricks

x = 0
y = 250 - HEIGHT

for q in range(5):
    x = (WIDTH + SPACE) * q
    color = colors[q]
    for b in range(x_number_bricks):
        bricks = brick.Brick(WIDTH, HEIGHT, GREEN, main_surface)
        bricks.draw_brick(x, y)
        x = x + WIDTH + SPACE
        pygame.display.update()
    x_number_bricks = x_number_bricks - 2
    y = y - HEIGHT - SPACE


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
