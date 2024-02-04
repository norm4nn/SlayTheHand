import pygame
from Cards.Card import Card

DEFAULT_CARD_WIDTH = 180
DEFAULT_CARD_HEIGHT = 240


def generateCard():
    rect = pygame.Rect(100, 100, DEFAULT_CARD_WIDTH, DEFAULT_CARD_HEIGHT)
    name = "Example name"
    desc = "Action"
    image = None
    return Card(rect, name, desc, image)
