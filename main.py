import pygame
import random
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans", 200)
my_font_two = pygame.font.SysFont("Comic Sans", 30)
pygame.display.set_caption("Farm")

# set up variables for the display
SCREEN_HEIGHT = 980
SCREEN_WIDTH = 1568
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
background = pygame.image.load("farm.png")
farm = pygame.image.load()
title = "Carrot"
start = "Play"
click = False

#rectangle
color = (255, 255, 255)
rectangle = pygame.Rect(778, 560, 60, 50)
pygame.draw.rect(background, color, pygame.Rect(768, 555, 75, 60))

#render
display_title = my_font.render(title, True, (0, 0, 0))
display_start = my_font_two.render(start, True, (0, 0, 0))

run = True

# -------- Main Program Loop -----------
while run:


    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rectangle.collidepoint(event.pos):
                click = True

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    if click == False:
        screen.blit(background, (0, 0))
        screen.blit(display_title, (500, 30))
        screen.blit(display_start, (780, 560))
    if click == True:
        screen.blit(, (0, 0))
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

