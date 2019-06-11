import pygame
import time
import random

#make head
class Head:
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
        self.direction = 0
        self.length=3
        self.updateCountMax = 2
        self.updateCount = 0
            for i in range(0,length):
        self.x.append(0)
        self.y.append(0)

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.speed
        if self.direction == 1:
            self.x = self.x - self.speed
        if self.direction == 2:
            self.y = self.y - self.speed
        if self.direction == 3:
            self.y = self.y + self.speed

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3
    
    #render script
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 

#define window

#main loop
while not done:



    #render
    screen.fill((0,0,0))


    pygame.display.flip()