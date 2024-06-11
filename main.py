import pygame
import random
from random import randint
from button import Button
from water import Water
from fish import Fish


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans", 200)
my_font_two = pygame.font.SysFont("Comic Sans", 30)
pygame.display.set_caption("Farm")

# set up variables for the display
# SCREEN_HEIGHT = 649
# SCREEN_WIDTH = 1152
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1300
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
start_button = pygame.image.load("play_button.png")
water = pygame.image.load("water.png")
# makes image transparent
water.set_alpha(200)
title = "Carrot"
start = "Play"
click = False

# rectangle = pygame.rect((0, 0, 1250, 750)
# rectangle.center = (576, 324.5)

# render
display_title = my_font.render(title, True, (0, 0, 0))
display_start = my_font_two.render(start, True, (0, 0, 0))

s = Button(645, 450)
fish = Fish(780, 450)

run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    clock.tick(60)
    if frame % 30 == 0:
        fish.switch_image()

    fish.move_fish()

    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:
            if s.rect.collidepoint(event.pos):
                click = True
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    if click == False:
        screen.fill((255, 255, 255))
        screen.blit(display_title, (500, 30))
        screen.blit(s.image, s.rect)
    if click == True:
        screen.fill((0, 0, 0))
        screen.blit(water, (0, 0))
        screen.blit(fish.image, fish.rect)

    frame += 1

    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

