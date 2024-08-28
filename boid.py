from vector import Vector
import pygame
import random
import math

class Boid:
    def __init__(self, x, y):

        self.position = Vector(x, y)

        angle = random.uniform(0, 2 * math.pi)
        self.velocity = Vector(0, 0)

        self.max_velocity = 500
        self.desired_separation = 20
        self.desired_neighbor_distance = 200

    def fly(self, boids):
        v1 = self.separate(boids) * 1.5
        v2 = self.align(boids)
        v3 = self.cohesion(boids)

        self.velocity = self.velocity + v1 + v2 + v3
        self.position = self.position + self.velocity * 0.001

        self.border()
   
    def border(self):
        self.position.x %= 1000
        self.position.y %= 1000
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), 5) 


    def limit_velocity(self):
        if self.velocity.magnitude() > self.max_velocity:
            self.velocity = (self.velocity / self.velocity.magnitude()) * self.max_velocity 

    def separate(self, boids):
        steer = Vector(0, 0)

        for boid in boids:
            if self.position.distance_to(boid.position) < self.desired_separation:
                steer = steer - (boid.position - self.position) 

        return steer
    
    def align(self, boids):
        steer = Vector(0, 0)

        for boid in boids:
            if self.position.distance_to(boid.position) < self.desired_neighbor_distance:
                steer = steer + boid.velocity

        steer = steer / (len(boids) - 1)

        return (steer - self.velocity) / 10
       
    def cohesion(self, boids):
        steer = Vector(0, 0)
            
        for boid in boids:
            if self.position.distance_to(boid.position) < self.desired_neighbor_distance:
                steer = steer + boid.position
        
        return steer / (len(boids) - 1)
            

                
                
                
                
        
