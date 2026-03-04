import pygame 
import sys 
import car
from assets import constants
pygame.init() 

WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT)) pygame.display.set_caption("Racing Game") 

clock = pygame.time.Clock() 

running = True while running: clock.tick(60) # 60 FPS 

for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
        running = False 
 
screen.fill((30, 30, 30))  # background color 
pygame.display.flip() 
  

pygame.quit() sys.exit() 

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