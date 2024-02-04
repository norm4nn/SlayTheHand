import pygame
from Engine.draw import draw
from Engine.input import input
from Engine.init import init


WIDTH = 1280
HEIGHT = 720

FPS_CAP = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("SlayTheHand")

running = True

hand = init()
objects = [hand]

while running:
    running = input(objects)

    draw(screen, objects)

    clock.tick(FPS_CAP)
