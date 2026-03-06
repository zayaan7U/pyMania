import pygame
import math
from functions import blit_rotate_center
import constants as c

class Car:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = c.CAR
        self.angle = 0
        self.velocity = 0
        self.acceleration = 0.2
        self.friction = 0.95
        self.max_speed = 5
        self.rotation_vel = 4

    def rotate(self,left=False,right=False):
        if left:
            self.angle += self.rotation_vel
        if right:
            self.angle -= self.rotation_vel

    def move_forward(self):
        self.velocity = min(self.velocity + self.acceleration,self.max_speed)
        self.move()

    def move_backward(self):
        self.velocity = max(self.velocity - self.acceleration,-self.max_speed/2)
        self.move()

    # tech with tim help to make the movement mechanics
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity
        horizontal = math.sin(radians) * self.velocity
        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.velocity *= self.friction
        if abs(self.velocity) < 0.05:
            self.velocity = 0
        self.move()

    def draw(self,screen):
        blit_rotate_center(screen,self.image,(self.x,self.y),self.angle)

    def collide(self,mask,x=0,y=0):
        car_mask = pygame.mask.from_surface(self.image)
        offset = (int(self.x-x),int(self.y-y))
        return mask.overlap(car_mask,offset)

    def bounce(self):
        self.velocity = -self.velocity
        self.move()