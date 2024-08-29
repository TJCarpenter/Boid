import pygame
import random
from boid import Boid
from grid import Grid

WIDTH, HEIGHT = 1000, 1000
NUM_BOIDS = 200
FPS = 60
GRID_SIZE = 50

def initialize_boids(num_boids, width, height):
    return [Boid(random.randint(51, width), random.randint(51, height)) for _ in range(num_boids)]

def update_boids(boids, grid, screen):
    grid.clear()
    for boid in boids:
        grid.add(boid)
        
    for boid in boids:
        neighbors = grid.get_neighbors(boid)
        boid.fly(neighbors)
        boid.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    boids = initialize_boids(NUM_BOIDS, WIDTH, HEIGHT)
    grid = Grid(WIDTH, HEIGHT, GRID_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        update_boids(boids, grid, screen)
        pygame.display.flip()  
        clock.tick(FPS)  

    pygame.quit()


if __name__ == "__main__":
    main()

