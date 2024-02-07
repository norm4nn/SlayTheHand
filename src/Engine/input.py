import pygame
from Engine.player import Player


def input(objects):
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            Player.add_card()

    return running
