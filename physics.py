import math
from particle import *

class Physics:
    def __init__(self, G):
        self.G = G

    def update(self, particles : list[Particle]):
        for i in range(len(particles)):
            mainParticle = particles[i]
            for j in range(len(particles)):
                if i == j:
                    continue
                otherParticle = particles[j]
                
                r = Particle.distance(mainParticle, otherParticle)
                F = self.G * mainParticle.m * otherParticle.m / (r ** 2)

                angleToOther = mainParticle.getAngleInRadsTo(otherParticle)

                mainParticle.dx -= F * math.cos(angleToOther) / mainParticle.m
                mainParticle.dy -= F * math.sin(angleToOther) / mainParticle.m

                otherParticle.dx += F * math.cos(angleToOther) / otherParticle.m
                otherParticle.dy += F * math.sin(angleToOther) / otherParticle.m