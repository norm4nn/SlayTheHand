import pygame
from Cards.Card import Card
from Engine.config import Config

def generateCard():
    rect = pygame.Rect(100, 100, Config.DEFAULT_CARD_WIDTH, Config.DEFAULT_CARD_HEIGHT)
    name = "Example name"
    desc = "Action"
    image = None
    return Card(rect, name, desc, image)
