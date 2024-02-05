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
        self.rotation_speed = 6

    def use(self):
        pass
        # TAKE SOME ACTION HERE

    def set_observer(self, observer):
        self.observer = observer

    def onclick(self):
        self.observer.use(self)

    def draw(self, screen):
        rotated_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        pygame.draw.rect(
            rotated_surface,
            colors.get_second_color(),
            (0, 0, self.rect.width, self.rect.height),
            border_radius=self.border_radius,
        )

        pygame.draw.rect(
            rotated_surface,
            colors.get_main_color(),
            (0, 0, self.rect.width, self.rect.height),
            border_radius=self.border_radius,
            width=2,
        )

        rotated_surface = pygame.transform.rotate(rotated_surface, self.rotation)

        rotated_rect = rotated_surface.get_rect(center=self.rect.center)

        screen.blit(rotated_surface, rotated_rect.topleft)

    def update(self, dt):
        self.update_position(dt)
        self.update_rotation(dt)

    def update_position(self, dt):
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

    def update_rotation(self, dt):
        if self.destination_rotation is not None:
            diff_rotation = self.destination_rotation - self.rotation
            self.rotation += diff_rotation * self.rotation_speed * dt
            abs_rotation = abs(self.destination_rotation - self.rotation)
            if abs_rotation < 0.01:
                self.destination_rotation = None

    def add_destination_rotation(self, destination_rotation):
        self.starting_rotation = self.rotation
        self.destination_rotation = destination_rotation

    def rotate_to(self, angle):
        self.destination_rotation = angle

    def add_destination_xy(self, destination):
        self.starting_xy = self.xy
        self.destination_xy = destination

    def reset_rotation(self):
        self.rotation = 0
        self.rotate_to = None
