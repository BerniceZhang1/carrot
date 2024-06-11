import pygame
import random
from random import randint

class Coordinate:

    def __init__(self, x, y):
        self.x = random.randint(-100, 1300)
        self.y = random.randint(-100, 750)
        if self.x <= 1300 and self.y == -100:
            self.side = top
        if self.x == -100 and self.y <= 750:
            self.side = left
        if self.x == 1300 and self.y <= 750:
            self.side = right
        if self.x <= 1300 and self.y == 750:
            self.side = bottom

        # (x, y) = random.randint(-100, 1300), -100
        # # left side
        # (x1, y1) = -100, random.randint(-100, 750)
        # # right_side
        # (x2, y2) = 1300, random.randint(-100, 750)
        # # bottom_side
        # (x3, y3) = random.randint(-100, 1300), 750