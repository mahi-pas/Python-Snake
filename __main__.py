import pygame
import time
import random
from snake import *

#initialize
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30) #change font sometime
screen = pygame.display.set_mode((1280,720))
done = False

#initial variables
p1_x,p1_y=30,30
#make objects
p1=Snake(p1_x,p1_y)

#main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    #Set controls p1
    

    #render frame
    screen.fill((0,0,0))
    p1.draw(screen)
    pygame.display.flip()