import pygame
import random
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans", 200)
my_font_two = pygame.font.SysFont("Comic Sans", 15)
pygame.display.set_caption("Farm")

# set up variables for the display
SCREEN_HEIGHT = 980
SCREEN_WIDTH = 1568
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
background = pygame.image.load("farm.png")
title = "Carrot"
left = "Store"
right = "Farm"
left_arrow = "<---"
right_arrow = "--->"

#render
display_title = my_font.render(title, True, (0, 0, 0))
display_left = my_font_two.render(left, True, (0, 0, 0))
display_right = my_font_two.render(right, True, (0, 0, 0))
display_left_arrow = my_font_two.render(left_arrow, True, (0, 0, 0))
display_right_arrow = my_font_two.render(right_arrow, True, (0, 0, 0))

run = True

# -------- Main Program Loop -----------
while run:


    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    screen.blit(background, (0, 0))
    screen.blit(display_title, (500, 30))
    screen.blit(display_left, (10, 490))
    screen.blit(display_right, (1510, 490))
    screen.blit(display_left_arrow, ())
    screen.blit(display_right_arrow, ())

    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

