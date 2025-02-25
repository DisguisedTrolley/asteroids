import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#ffffff", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(rand_angle)
        vec2 = self.velocity.rotate(-rand_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        small_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        small_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

        small_ast_1.velocity = vec1 * 1.2
        small_ast_2.velocity = vec2 * 1.2
