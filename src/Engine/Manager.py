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
        UpdateManager.add_updateable_object(object)
        InputManager.add_object(object)
        DrawManager.add_drawable_object(object)
