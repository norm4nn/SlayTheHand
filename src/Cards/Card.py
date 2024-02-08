from Colors import colors
from Engine.config import Config
import pygame


class Card:
    def __init__(self, rect, name, desc, image):
        self.rect = rect
        self.name = name
        self.desc = desc
        self.image = image
        self.is_hovered = False
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
        self.scale = 1
        self.destination_scale = None
        self.starting_scale = None
        self.scale_change_speed = 6

    def use(self):
        pass
        # TAKE SOME ACTION HERE

    def set_observer(self, observer):
        self.observer = observer

    def onclick(self):
        self.observer.use(self)

    def draw(self, screen):
        dummy_rect = pygame.Rect(self.rect)
        dummy_rect.width *= self.scale
        dummy_rect.height *= self.scale
        rotated_surface = pygame.Surface(dummy_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(
            rotated_surface,
            colors.get_second_color(),
            (0, 0, self.rect.width * self.scale, self.rect.height * self.scale),
            border_radius=self.border_radius,
        )

        pygame.draw.rect(
            rotated_surface,
            colors.get_main_color(),
            (0, 0, self.rect.width * self.scale, self.rect.height * self.scale),
            border_radius=self.border_radius,
            width=2,
        )

        rotated_surface = pygame.transform.rotate(rotated_surface, self.rotation)

        rotated_rect = rotated_surface.get_rect(center=self.rect.center)

        screen.blit(rotated_surface, rotated_rect.topleft)

    def update(self, dt):
        self.update_scale(dt)
        self.update_position(dt)
        self.update_rotation(dt)

    def detected_hover(self):
        dummy_rect = pygame.Rect(self.rect)
        dummy_rect.width *= self.scale
        dummy_rect.height *= self.scale

        mouse_pos = pygame.mouse.get_pos()
        return dummy_rect.collidepoint(mouse_pos)

    def update_scale(self, dt):
        if self.destination_scale is not None:
            diff = self.destination_scale - self.scale
            self.scale += diff * self.scale_change_speed * dt

            if abs(diff) < 0.01:
                self.destination_scale = None

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

    def set_destination_rotation(self, destination_rotation):
        self.starting_rotation = self.rotation
        self.destination_rotation = destination_rotation

    def rotate_to(self, angle):
        self.destination_rotation = angle

    def set_destination_xy(self, destination):
        self.starting_xy = self.xy
        self.destination_xy = destination

    def reset_rotation(self):
        self.rotation = 0
        self.rotate_to = None

    def set_scale_destination(self, scale_to):
        self.destination_scale = scale_to
        self.starting_scale = self.scale

    def move_by_vector(self, vector):
        self.set_destination_xy(
            (
                self.xy[0] + vector[0],
                self.xy[1] + vector[1],
            )
        )

    def hover(self):
        if not self.is_hovered:
            self.set_scale_destination(1.5)
            self.set_destination_xy(
                (self.xy[0], Config.HEIGHT - 1.25 * self.rect.height)
            )
            self.set_destination_rotation(0)
            self.is_hovered = True

    def unhover(self):
        if self.is_hovered:
            self.set_scale_destination(1)
            self.is_hovered = False

    def input(self):
        if self.detected_hover():
            self.observer.hovered_card(self)
        elif self.is_hovered:
            self.observer.unhovered_card(self)

        if self.detected_hover() and self.is_hovered and pygame.mouse.get_pressed()[0]:
            self.observer.discard(self)
