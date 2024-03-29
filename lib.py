# Copyright (c) 2024, Kason Suchow <kason.suchow@gmail.com>

# python module imports
import pygame
from random import randint

# constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "bh"

class Colors:
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)

    def random(self) -> pygame.Color:
        color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255), 255)

        return color
    
    def random_gray(self) -> pygame.Color:
        scale = randint(0, 255) # determine the random scale

        color = pygame.Color(scale, scale, scale, 255)

        return color
    
    def random_custom(self, channels: str) -> pygame.Color:
        red_channel = 0
        green_channel = 0
        blue_channel = 0
        
        if 'r' in channels:
            red_channel = randint(0, 255)
        if 'g' in channels:
            green_channel = randint(0, 255)
        if 'b' in channels:
            blue_channel = randint(0, 255)

        color = pygame.Color(red_channel, green_channel, blue_channel, 255)

        return color
        

color = Colors() # color object for reference in other files

# initialize game loop stuff
delta_time = 0
events = None
framerate = 120

# camera stuff
global_offset = pygame.math.Vector2(0, 0)