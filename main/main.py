import pygame 
import sys 
import car
import constants

  
pygame.init() 

width = constants.WIDTH
height = constants.HEIGHT

screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Racing Game") 

clock = pygame.time.Clock() 

car = Car((width - 50)//2, height - 30)  # centered horizontally at the bottom of the screen

running = True
while running:
    clock.tick(60)  # 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()

    # Update
    car.move(keys, width)

    # Draw
    screen.fill((30, 30, 30))  # background
    car.draw(screen)
    pygame.display.flip()
pygame.quit() 
sys.exit()
