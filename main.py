import pygame
import random
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Times New Roman", 15)
pygame.display.set_caption("Farm")

# set up variables for the display
SCREEN_HEIGHT = 980
SCREEN_WIDTH = 1568
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
background = pygame.image.load("farm.png")

r = 255
g = 255
b = 255

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

    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

