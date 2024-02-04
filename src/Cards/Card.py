from Colors import colors
import pygame


class Card:
    def __init__(self, rect, name, desc, image):
        self.rect = rect
        self.name = name
        self.desc = desc
        self.image = image
        self.hover = False
        self.observer = None
        self.border_radius = int(0.1 * self.rect.width)

    def use(self):
        pass
        # TAKE SOME ACTION HERE

    def set_observer(self, observer):
        self.observer = observer

    def onclick(self):
        self.observer.use(self)

    def draw(self, screen):
        shadow_rect = pygame.Rect(self.rect)
        shadow_rect = shadow_rect.move(0.03 * self.rect.width, 0.03 * self.rect.height)
        pygame.draw.rect(
            screen, colors.get_shadow(), shadow_rect, border_radius=self.border_radius
        )
        pygame.draw.rect(
            screen,
            colors.get_second_color(),
            self.rect,
            border_radius=self.border_radius,
        )

    def update():
        pass  # TO DO
