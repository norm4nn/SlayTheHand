import pygame
from Engine.draw import draw
from Engine.input import input


WIDTH = 1280
HEIGHT = 720

FPS_CAP = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("SlayTheHand")

running = True

while running:
    running = input()

    draw(screen)

    clock.tick(FPS_CAP)
