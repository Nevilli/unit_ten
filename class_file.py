# Liam Neville
# 12/11/18
# This program draws a 5 layer brick pyramid of different colors


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
# Window dimensions
main_surface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Brick pyramid")

# This calculates the width of the bricks
WIDTH = (500 - (x_number_bricks * SPACE))/x_number_bricks

x = 0
y = 250 - HEIGHT

# This double loop draws the bricks in 5 rows of different colors
for q in range(5):
    x = (WIDTH + SPACE) * q
    color = colors[q]
    for b in range(x_number_bricks):
        bricks = brick.Brick(WIDTH, HEIGHT, color, main_surface)
        bricks.draw_brick(x, y)
        # This changes the x coordinate for the bricks in each row
        x = x + WIDTH + SPACE
        pygame.display.update()
    x_number_bricks = x_number_bricks - 2
    # This changes the y coordinate for the bricks in each row
    y = y - HEIGHT - SPACE


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
