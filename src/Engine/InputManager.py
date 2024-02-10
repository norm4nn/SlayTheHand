import pygame
from Engine.Player import Player


class InputManager:

    objects = []

    def input():
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                Player.add_card()

        for object in InputManager.objects:
            object.input()
        return running

    @staticmethod
    def add_object(object):
        InputManager.objects.append(object)

    @staticmethod
    def remove_object(object):
        InputManager.objects.remove(object)
