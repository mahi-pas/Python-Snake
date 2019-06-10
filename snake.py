import pygame
import time
import random

#make head
class Head:
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

#define window

#main loop
while not done:



    #render
    screen.fill((0,0,0))


    pygame.display.flip()