import pygame
import sys
import constants as c
from car import Car

pygame.init()

screen = pygame.display.set_mode((c.WIDTH,c.HEIGHT))
pygame.display.set_caption("Racing Game")

clock = pygame.time.Clock()

car = Car(180,200)

running = True

while running:

    clock.tick(c.FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    moved = False

    if keys[pygame.K_a]:
        car.rotate(left=True)

    if keys[pygame.K_d]:
        car.rotate(right=True)

    if keys[pygame.K_w]:
        moved = True
        car.move_forward()

    if keys[pygame.K_s]:
        moved = True
        car.move_backward()

    if not moved:
        car.reduce_speed()


    # COLLISION
    if car.collide(c.TRACK_BORDER_MASK) != None:
        car.bounce()


    # DRAW
    screen.blit(c.GRASS,(0,0))
    screen.blit(c.TRACK,(0,0))
    screen.blit(c.FINISH,c.FINISH_POSITION)
    screen.blit(c.TRACK_BORDER,(0,0))

    car.draw(screen)

    pygame.display.update()


pygame.quit()
sys.exit()