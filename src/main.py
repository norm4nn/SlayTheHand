import pygame
from Engine.draw import draw
from Engine.input import input
from Engine.update import update
from Engine.player import Player
from Engine.config import Config


pygame.init()

screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption(Config.TITLE)

running = True

hand = Player.hand
objects = [hand]

while running:
    running = input(objects)

    draw(screen, objects)

    dt = clock.tick(Config.FPS_CAP) / 1000
    update(objects, dt)
