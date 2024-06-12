import pygame
import random
from random import randint
from button import Button
from water import Water
from fish import Fish
import random

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont("inkfree", 220)

print(pygame.font.get_fonts())
pygame.display.set_caption("Farm")

# set up variables for the display
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 1200
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
background = pygame.image.load("background.png")
start_button = pygame.image.load("play_button.png")
water = pygame.image.load("water.png")
# makes image transparent
water.set_alpha(250)
# title = "𝐿𝑒 𝒫𝑜𝒾𝓈𝓈𝑜𝓃"
title = "Le Poisson"
click = False


# render
display_title = my_font.render(title, True, (255, 255, 255))


s = Button(475, 400)
fish = Fish(size)
# fish = Fish(780, 450, size)


fishes = []

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

    for fish in fishes:
        Fish.check_reached_coord(fish)
        # if not (fish.reached_coord):
        if not(Fish.check_reached_coord):
            Fish.move_fish(fish)
        else:
            fishes.pop(fishes.index(fish))

    for fish in fishes:
        screen.blit(fish.image, fish.rect)

    if len(fishes) < 4:
        fishes.append(Fish(size))

    ## FILL SCREEN, and BLIT here ##
    if click == False:
        screen.blit(background, (0, 0))
        screen.blit(display_title, (120, 130))
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

