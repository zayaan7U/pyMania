import pygame
import constants as c

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.color = (200, 0, 0)
        self.velocity = 0       # current speed
        self.acceleration = 0.5 
        self.friction = 0.9     # deceleration for real world mechanics
        self.max_speed = 10

    def move(self, keys, screen_width):
        # acceleration input
        if keys[pygame.K_RIGHT]:
            self.velocity += self.acceleration
        elif keys[pygame.K_LEFT]:
            self.velocity -= self.acceleration
        else:
            # apply friction
            self.velocity *= self.friction

        # makes velocity not exceed max speed
        if self.velocity > self.max_speed:
            self.velocity = self.max_speed
        if self.velocity < -self.max_speed:
            self.velocity = -self.max_speed

        # deadzone to make sure car can stop instead of always moving due to friction deceleration
        if abs(self.velocity) < 0.1:
            self.velocity = 0

        # update position
        self.x += self.velocity

        # boundary check
        if self.x < 0:
            self.x = 0
            self.velocity = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
            self.velocity = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
