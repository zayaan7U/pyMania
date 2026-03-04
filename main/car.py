import pygame
class Car: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        self.width = 50 
        self.height = 30 
        self.color = (200, 0, 0) 
        self.speed = 5 
    def draw(self, screen): 
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height)) 
 
    def move(self, keys): 
        if keys[pygame.K_LEFT]: 
            self.x -= self.speed 
        if keys[pygame.K_RIGHT]: 
            self.x += self.speed