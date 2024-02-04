import pygame
from Colors import colors


def draw(screen):
    draw_background(screen)
    pygame.display.update()


def draw_background(screen):
    screen.fill(colors.get_background_color())
