import pygame
import math
from boid import Boid
import random 

pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))

boids = []
for _ in range(100):
    x = random.randint(51, WIDTH)
    y = random.randint(51, HEIGHT)
    boids.append(Boid(x, y))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    for boid in boids:
        boid.fly(boids)
        boid.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()

