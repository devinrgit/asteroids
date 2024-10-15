from pygame import *
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)