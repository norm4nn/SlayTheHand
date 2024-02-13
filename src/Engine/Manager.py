from Engine.UpdateManager import UpdateManager
from Engine.InputManager import InputManager
from Engine.DrawManager import DrawManager


class Manager:
    @staticmethod
    def add_object(object):
        UpdateManager.add_updateable_object(object)
        InputManager.add_object(object)
        DrawManager.add_drawable_object(object)

    @staticmethod
    def remove_object(object):
        UpdateManager.remove_updateable_object(object)
        InputManager.remove_object(object)
        DrawManager.remove_drawable_object(object)

    @staticmethod
    def input():
        return InputManager.input()

    @staticmethod
    def draw():
        DrawManager.draw()

    @staticmethod
    def update(dt):
        UpdateManager.update(dt)

    @staticmethod
    def set_screen(screen):
        DrawManager.screen = screen
