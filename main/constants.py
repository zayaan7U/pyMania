import pygame
from functions import scale_image

pygame.init()

GRASS = scale_image(pygame.image.load("main/imgs/grass.jpg"),2.5)
TRACK = scale_image(pygame.image.load("main/imgs/track.png"),0.9)

TRACK_BORDER = scale_image(pygame.image.load("main/imgs/track-border.png",), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

FINISH = pygame.image.load("main/imgs/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (130,250)

CAR = scale_image(pygame.image.load("main/imgs/red-car.png"),0.55) #0.6 seemed too big and 0.5 seemed too small

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
FPS = 60