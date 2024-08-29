import pygame
import math
import random
from vector import Vector

class Preditor:

    def __init__(self, x, y):
        
        self.position = Vector(x, y)
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(5, 10)
        self.velocity = Vector(math.cos(angle) * speed, math.sin(angle) * speed)

        self.max_velocity = 2
        self.min_velocity = 1

        self.desired_separation = 30
        self.hunting_distance = 100
        self.border_margin = 100

        self.color = (255, 0, 0)
        self.radius = 7
        
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (10, 10), 7)

    def fly(self, boids):
        v1 = self.hunt(boids)
        v2 = self.separate(boids)
        v3 = self.contain()        

        self.velocity = self.velocity + v1 + v2 + v3
        self.limit_velocity()
        self.position = self.position + self.velocity

    def separate(self, boids):
        steer = Vector(0, 0)
        count = 0

        for boid in boids:
            if boid is self or not isinstance(boid, Preditor):
                continue
            
            distance = self.position.distance_to(boid.position)
            if distance < self.desired_separation:
                diff = self.position - boid.position
                diff /= distance
                steer += diff
                count += 1

        if count > 0:
            steer /= count
            steer.normalize()
            steer *= self.max_velocity

        return steer

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))

    def hunt(self, boids):
        steer = Vector(0, 0)
        count = 0

        for boid in boids:
            if boid is self or not isinstance(self, Preditor):
                continue
                        
            if self.position.distance_to(boid.position) < self.hunting_distance:
                steer = steer + boid.position
                count += 1
        
        if count > 0:
            steer /= count
            steer -= self.position
            steer.normalize()
            steer *= self.max_velocity

        return steer / 100

    def contain(self):
        steer = Vector(0, 0)

        if self.position.x < self.border_margin:
            steer.x += (self.border_margin - self.position.x) / self.border_margin
        elif self.position.x > 1000 - self.border_margin:
            steer.x -= (self.position.x - (1000 - self.border_margin)) / self.border_margin

        if self.position.y < self.border_margin:
            steer.y += (self.border_margin - self.position.y) / self.border_margin
        elif self.position.y > 1000 - self.border_margin:
            steer.y -= (self.position.y - (1000 - self.border_margin)) / self.border_margin

        return steer

    def limit_velocity(self):
        if self.velocity.magnitude() > self.max_velocity:
            self.velocity = (self.velocity / self.velocity.magnitude()) * self.max_velocity
        elif self.velocity.magnitude() < self.min_velocity:
            self.velocity = (self.velocity / self.velocity.magnitude()) * self.min_velocity
