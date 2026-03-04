import pygame 
import sys 
import car
import constants

  
pygame.init() 

WIDTH = constants.WIDTH
HEIGHT = constants.HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Racing Game") 

clock = pygame.time.Clock() 

running = True
while running: 
  clock.tick(60) # 60 FPS 

  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
        running = False 
 
  screen.fill((30, 30, 30))  # background color 
  pygame.display.flip() 
  

pygame.quit() 
sys.exit() 



