import pygame
from Engine.draw import draw
from Engine.input import input
from Engine.update import update
from Engine.engine import Engine
from Engine.config import Config


WIDTH = 1280
HEIGHT = 720
FPS_CAP = 60

pygame.init()

screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("SlayTheHand")

running = True

hand = Engine.hand
objects = [hand]

while running:
    running = input(objects)

    draw(screen, objects)

    dt = clock.tick(Config.FPS_CAP) / 1000
    update(objects, dt)
