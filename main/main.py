import pygame
import sys
import constants as c
from car import Car
import functions as f
pygame.init()

screen = pygame.display.set_mode((c.WIDTH,c.HEIGHT))
pygame.display.set_caption("Racing Game")

clock = pygame.time.Clock()

car = Car(180,200)

start_ticks = pygame.time.get_ticks()
font = pygame.font.Font(None, 30)

#  timer
def format_time(ms: int) -> str:
    seconds = ms / 1000
    minutes = int(seconds // 60)
    seconds = seconds % 60
    return f"{minutes}:{seconds:05.2f}"

lap_count = 0
lap_start_ticks = start_ticks
last_lap_time = None
best_lap_time = None
finished_last_frame = False

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

    # collision with track border
    if car.collide(c.TRACK_BORDER_MASK) != None:
        car.bounce()

    # lap/finish line tracking
    on_finish = car.collide(c.FINISH_MASK, *c.FINISH_POSITION) != None
    if on_finish and not finished_last_frame:
        now = pygame.time.get_ticks()
        lap_time = now - lap_start_ticks
        lap_start_ticks = now
        lap_count += 1
        last_lap_time = lap_time
        if best_lap_time is None or lap_time < best_lap_time:
            best_lap_time = lap_time
    finished_last_frame = on_finish

    # output
    screen.blit(c.GRASS,(0,0))
    screen.blit(c.TRACK,(0,0))
    screen.blit(c.FINISH,c.FINISH_POSITION)
    screen.blit(c.TRACK_BORDER,(0,0))
    car.draw(screen)

    elapsed_ms = pygame.time.get_ticks() - start_ticks
    elapsed_sec = elapsed_ms // 1000
    timer_text = font.render(f"Time: {elapsed_sec}s", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    lap_text = font.render(f"Lap: {lap_count}", True, (255, 255, 255))
    screen.blit(lap_text, (10, 40))

    if last_lap_time is not None:
        last_text = font.render(f"Last: {format_time(last_lap_time)}", True, (255, 255, 255))
        screen.blit(last_text, (10, 70))

    if best_lap_time is not None:
        best_text = font.render(f"Best: {format_time(best_lap_time)}", True, (255, 255, 255))
        screen.blit(best_text, (10, 100))

    pygame.display.update()

pygame.quit()
sys.exit()
