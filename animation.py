import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

white = (255, 255, 255)
man_Img = pygame.image.load('man.png')
manx = 10
many = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(white)

    if direction == 'right':
        manx += 5
        if manx == 280:
            direction = 'down'
    elif direction == 'down':
        many += 5
        if many == 220:
            direction = 'left'
    elif direction == 'left':
        manx -= 5
        if manx == 10:
            direction = 'up'
    elif direction == 'up':
        many -= 5
        if many == 10:
            direction = 'right'

    DISPLAYSURF.blit(man_Img, (manx, many))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)