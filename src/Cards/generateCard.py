import pygame
from Cards.Card import Card

DEFAULT_CARD_WIDTH = 120
DEFAULT_CARD_HEIGHT = 180


def generateCard():
    rect = pygame.Rect(0, 0, DEFAULT_CARD_WIDTH, DEFAULT_CARD_HEIGHT)
    name = "Example name"
    desc = "Action"
    image = None
    return Card(rect, name, desc, image)
