import pygame
from particle import *

class CollisionController:
    def __init__(self, edges : pygame.Rect):
        self.edges = edges

    def move(self, particles : list[Particle]):
        self.moveHorizontally(particles)
        self.moveVertically(particles)

    def moveHorizontally(self, particles : list[Particle]):
        for p in particles:
            if (p.dx < 0 and p.dx > p.x - self.edges.left) or (
                p.dx > 0 and p.dx > self.edges.right - p.x + p.size):
                p.dx *= -1
            p.x += p.dx

    def moveVertically(self, particles : list[Particle]):
        for p in particles:
            if (p.dy < 0 and p.dy > p.y - self.edges.top) or (
                p.dy > 0 and p.dy > self.edges.bottom - p.y + p.size):
                p.dy *= -1
            p.y += p.dy