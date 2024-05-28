import pygame
import random
import time
from button import Button
from bath_tub import Bathtub


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans", 200)
my_font_two = pygame.font.SysFont("Comic Sans", 30)
pygame.display.set_caption("Farm")

# set up variables for the display
SCREEN_HEIGHT = 950
SCREEN_WIDTH = 1500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
# background = pygame.image.load("farm.png")
start_button = pygame.image.load("play_button.png")
bathtub = pygame.image.load("bath_tub.png")
# farm = pygame.image.load()
title = "Carrot"
start = "Play"
click = False
start_time = time.time()

#render
display_title = my_font.render(title, True, (0, 0, 0))
display_start = my_font_two.render(start, True, (0, 0, 0))

s = Button(680, 520)

run = True

# -------- Main Program Loop -----------
while run:


    # --- Main event loop
    current_time = time.time()
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
        # screen.blit(background, (0, 0))
        screen.fill((255, 255, 255))
        screen.blit(display_title, (500, 30))
        screen.blit(s.image, s.rect)
    if click == True:
        screen.fill((0, 0, 0))
        screen.blit(bathtub, (500, 500))
        current_time = time.time()
        time_elapsed = round(10 - (current_time - start_time), 2)
        display_time = my_font_two.render("Time Elapsed: " + str(time_elapsed) + "s", True, (255, 255, 255))
        screen.blit(display_time, (0, 30))

        # screen.blit(, (0, 0))
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

