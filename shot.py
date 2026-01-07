#import libraries
import pygame

#import modules
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, SHOT_RADIUS)
    
    def update(self, dt):
        self.position += (self.velocity*dt)
    
    def rotate(self, other):
        self.position == other.position