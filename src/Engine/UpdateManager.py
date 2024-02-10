class UpdateManager:
    updateables = []

    @staticmethod
    def update(dt):
        for object in UpdateManager.updateables:
            object.update(dt)

    @staticmethod
    def add_updateable_object(updateable):
        UpdateManager.updateables.append(updateable)

    @staticmethod
    def remove_updateable_object(updateable):
        UpdateManager.updateables.remove(updateable)
