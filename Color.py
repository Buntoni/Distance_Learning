import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors

black = (  0,   0,   0)
white = (255, 255, 255)
red = (255,   0,   0)
green = (  0, 255,   0)
blue = (  0,   0, 255)


# draw on the surface object

DISPLAYSURF.fill(white)

pygame.draw.polygon(DISPLAYSURF, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

pygame.draw.line(DISPLAYSURF, blue, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, blue, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, blue, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, blue, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, red, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, red, (200, 150, 100, 50))



pixObj = pygame.PixelArray(DISPLAYSURF)

pixObj[480][380] = black

pixObj[482][382] = black

pixObj[484][384] = black

pixObj[486][386] = black

pixObj[488][388] = black

del pixObj

# run the game loop

while True:
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
     pygame.display.update()