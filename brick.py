# Liam Neville
# 12/11/18
# This program creates the bricks that will be drawn in the class_file


import pygame


class Brick:

    def __init__(self, width, height, color, main_surface):
        """
        This function includes all of the measurements and variables for the bricks
        :param width: width of brick
        :param height: height of brick
        :param color: color of brick
        :param main_surface: surface where the brick would be drawn
        """
        self.main_surface = main_surface
        self.width = width
        self.height = height
        self.color = color

    def draw_brick(self, x, y):
        """
        This function draws the bricks
        :param x: x coordinate
        :param y: y coordinate
        :return: none
        """
        pygame.draw.rect(self.main_surface, self.color, (x, y, self.width, self.height), 0)
        pygame.display.update()
