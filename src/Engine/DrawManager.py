import pygame
from Colors import colors


class DrawManager:

    drawables = []
    screen = None

    @staticmethod
    def draw():
        DrawManager.draw_background()

        for drawable in DrawManager.drawables:
            drawable.draw(DrawManager.screen)

        pygame.display.update()

    @staticmethod
    def draw_background():
        DrawManager.screen.fill(colors.get_background_color())

    @staticmethod
    def add_drawable_object(drawable):
        DrawManager.drawables.append(drawable)
