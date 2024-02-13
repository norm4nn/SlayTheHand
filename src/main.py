import pygame
from Engine.Manager import Manager
from Engine.Player import Player
from Engine.config import Config


pygame.init()

screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption(Config.TITLE)

running = True

hand = Player.hand
Manager.set_screen(screen)
Manager.add_object(hand)

while running:
    running = Manager.input()

    Manager.draw()

    dt = clock.tick(Config.FPS_CAP) / 1000
    Manager.update(dt)
