import pygame
from lib import *
from particle import *
from physics import *
from collisionController import *
from random import randint

WIDTH = 720
HEIGHT = 620
FPS = 30 

EDGES = False
COLORIZED = False

def generateParticles(cols, size, x, y, padding, mFrom, mTo):
    res = []
    for i in range(cols):
        for j in range(cols):
            m = randint(mFrom, mTo)

            color = colors['white']
            global COLORIZED
            if COLORIZED:
                percent = (m - mFrom) / (mTo - mFrom)

                # зеленый - мин. масса, красный - максимальная
                color = (255 * (percent), 255 * (1 - percent), 0)

            res.append(
                Particle(
                    size,
                    x + size + j*padding, 
                    y + size + i*padding, 
                    m,
                    screen,
                    color
            ))
    return res

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulator")
clock = pygame.time.Clock()

particles = generateParticles(10, 1, 200, 200, 10, 5, 10)
physics = Physics(0.1)
collisionController = CollisionController(pygame.Rect(0, 0, WIDTH, HEIGHT))

running = True
while running:         
    clock.tick(FPS)   
    
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            running = False
    
    # логика
    physics.update(particles)

    if EDGES:
        collisionController.move(particles)
    else:
        for p in particles:
            p.update()

    # предварительная отрисовка
    screen.fill(colors["black"])
    
    for p in particles:
        p.draw()

    # показываем кадр
    pygame.display.flip()       

pygame.quit()