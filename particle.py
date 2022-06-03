import math
import pygame
from lib import *

particlesCreated = 0
class Particle:
    def __init__(self, size, x, y, m, screen : pygame.Surface, color=colors['white']):
        self.size = size
        self.x = x
        self.y = y
        self.m = m
        self.screen = screen
        self.color = color

        self.dx = 0
        self.dy = 0

        global particlesCreated
        particlesCreated += 1

        self.id = particlesCreated

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))

    def distance(p1, p2):
        return math.hypot((p1.x - p2.x), (p1.y - p2.y))

    def getDirectionInRads(self):
        angle = math.acos(self.dx / math.hypot(self.dx, self.dy))
        if self.dy > 0:
            angle *= -1
        return angle

    def getAngleInRadsTo(self, other):
        deltaW = (self.x - other.x)
        deltaH = (self.y - other.y)
        distance = math.hypot(deltaW, deltaH)
        angle = math.acos(math.fabs(deltaW) / distance)
        if deltaW < 0 and deltaH > 0:
            angle = math.pi - angle
        elif deltaW < 0 and deltaH < 0:
            angle = math.pi + angle
        elif deltaW > 0 and deltaH < 0:
            angle = 2*math.pi - angle
        return angle

    def update(self):
        self.x += self.dx
        self.y += self.dy