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
        self.xy = (rect.x, rect.y)
        self.rotation = 0
        self.destination_xy = None
        self.starting_xy = None
        self.destination_rotation = None
        self.starting_rotation = None
        self.translation_speed = 4

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

    def update(self, dt):
        if self.destination_xy is not None:
            diff_x = self.destination_xy[0] - self.xy[0]
            diff_y = self.destination_xy[1] - self.xy[1]
            self.xy = (
                self.xy[0] + diff_x * self.translation_speed * dt,
                self.xy[1] + diff_y * self.translation_speed * dt,
            )
            abs_x = abs(self.destination_xy[0] - self.xy[0])
            abs_y = abs(self.destination_xy[1] - self.xy[1])
            if abs_x < 0.1 and abs_y < 0.1:
                self.destination_xy = None

        self.rect.x, self.rect.y = self.xy

    def add_destination_xy(self, destination):
        self.starting_xy = self.xy
        self.destination_xy = destination
