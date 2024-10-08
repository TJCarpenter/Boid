from vector import Vector
from preditor import Preditor
import pygame
import random
import math

class Boid:
    def __init__(self, x, y):

        self.position = Vector(x, y)

        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(5, 10)
        self.velocity = Vector(math.cos(angle) * speed, math.sin(angle) * speed)
        
        self.radius = 5
        self.max_velocity = 3
        self.min_velocity = 1
        self.desired_separation = 15
        self.desired_neighbor_distance = 50
        self.avoid_distance = 50
        self.border_margin = 50
        
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (5, 5), 5)

    def fly(self, boids):
        v1 = self.separate(boids) * 0.3
        v2 = self.align(boids) * 0.25
        v3 = self.cohesion(boids) * 0.25
        v4 = self.contain() * 0.125
        v5 = self.avoid(boids)
        
        self.velocity = self.velocity + v1 + v2 + v3 + v4 + v5
        self.limit_velocity()
        self.position = self.position + self.velocity

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))

    def limit_velocity(self):
        if self.velocity.magnitude() > self.max_velocity:
            self.velocity = (self.velocity / self.velocity.magnitude()) * self.max_velocity
        elif self.velocity.magnitude() < self.min_velocity:
            self.velocity = (self.velocity / self.velocity.magnitude()) * self.min_velocity
            
    def separate(self, boids):
        steer = Vector(0, 0)
        count = 0

        for boid in boids:
            if boid is self or not isinstance(boid, Boid):
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
    
    def align(self, boids):
        steer = Vector(0, 0)
        count = 0

        for boid in boids:
            if boid is self or not isinstance(boid, Boid):
                continue

            if self.position.distance_to(boid.position) < self.desired_neighbor_distance:
                steer = steer + boid.velocity
                count += 1

        if count > 0:
            steer /= count 
            steer -= self.velocity
            steer.normalize()
            steer *= self.max_velocity
            
        return steer / 10
       
    def cohesion(self, boids):
        steer = Vector(0, 0)
        count = 0 

        for boid in boids:
            if not isinstance(boid, Boid):
                continue

            if self.position.distance_to(boid.position) < self.desired_neighbor_distance:
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

                
    def avoid(self, boids):
        steer = Vector(0, 0)
        count = 0

        for boid in boids:
            if boid is self:
                continue

            distance = self.position.distance_to(boid.position)

            if isinstance(boid, Preditor) and distance < self.avoid_distance:
                diff = self.position - boid.position
                diff /= distance
                steer += diff

                count += 1

        return steer
