import pygame
import random
from random import randint
class Fish:

    def __init__(self, screen_dimensions):
        self.screen_dimensions = screen_dimensions

        self.dir_going = random.randint(0, 3)
        self.direction = ["left", "right", "down", "up"][self.dir_going]
        self.image_list = ["fish-left-up.png", "fish-right-up.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.starting_pos = [(self.screen_dimensions[0], random.randint(0, self.screen_dimensions[1] - self.image_size[1])),
        (-self.image_size[0], random.randint(0, self.screen_dimensions[1] - self.image_size[1])),
        (random.randint(0, self.screen_dimensions[0] - self.image_size[0]), -self.image_size[1]),
        (random.randint(0, self.screen_dimensions[0] - self.image_size[0]), self.screen_dimensions[1])
        ]
        self.x = starting_pos[self.dir_going][0]
        self.y = starting_pos[self.dir_going][1]
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2
        self.left = True
        self.reached_coord = False
    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .1, self.image_size[1] * .1)
        self.image = pygame.transform.scale(self.image, scale_size)

    def check_reached_coord(self):
        if self.direction == "left":
            if self.x <= -self.image_size[0]:
                self.reached_coord = True
        elif self.direction == "right":
            if self.x >= self.screen_dimensions[0]:
                self.reached_coord = True
        elif self.direction == "up":
            if self.y <= -self.image_size[1]:
                self.reached_coord = True
        else:
            if self.y >= self.screen_dimensions[1]:
                self.reached_coord = True

    def move_fish(self):
        if self.direction == "left":
            self.x -= self.delta
        elif self.direction == "right":
            self.x += self.delta
        elif self.direction == "up":
            self.y -= self.delta
        elif self.direction == "down":
            self.y += self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def fish_position(self):
        self.x = random.randint(-100, 1300)
        self.y = random.randint(-100, 750)
        if self.x <= 1300 and self.y == -100:
            side = top
        if self.x == -100 and self.y <= 750:
            side = left
        if self.x == 1300 and self.y <= 750:
            side = right
        if self.x <= 1300 and self.y == 750:
            side = bottom

    def switch_image(self, side):
        if side == top:
            if not self.left:
                image_number = 1
            self.image = pygame.image.load(self.image_list[image_number])
            # self.rescale_image(self.image)
            self.image_size = self.image.get_size()
            self.left = not self.left

        if side == bottom:
            image_number = 0
            if not self.left:
                image_number = 1
            self.image = pygame.image.load(self.image_list[image_number])
            # self.rescale_image(self.image)
            self.image_size = self.image.get_size()
            self.left = not self.left



