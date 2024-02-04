import pygame
from Colors import colors


def draw(screen, objects):
    draw_background(screen)

    for object in objects:
        object.draw(screen)

    pygame.display.update()


def draw_background(screen):
    screen.fill(colors.get_background_color())
