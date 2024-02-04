import pygame


def input(objects):
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    return running
