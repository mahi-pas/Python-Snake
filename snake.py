import pygame
import time
import random

#snake class
class Snake:
    #Macros
    len=30

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.length=3
        self.dir=0
        self.speed=2

    def update(self):
        if self.direction == 0:
            self.x += self.speed
        if self.direction == 1:
            self.x -= self.speed
        if self.direction == 2:
            self.y -= self.speed
        if self.direction == 3:
            self.y += self.speed

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self,screen):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,len,len))
        self.update()