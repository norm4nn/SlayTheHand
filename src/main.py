import pygame
from Engine.DrawManager import DrawManager
from Engine.InputManager import InputManager
from Engine.UpdateManager import UpdateManager
from Engine.Manager import Manager
from Engine.Player import Player
from Engine.config import Config


pygame.init()

screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption(Config.TITLE)

running = True

hand = Player.hand
DrawManager.screen = screen
Manager.add_object(hand)

while running:
    running = InputManager.input()

    DrawManager.draw()

    dt = clock.tick(Config.FPS_CAP) / 1000
    UpdateManager.update(dt)
