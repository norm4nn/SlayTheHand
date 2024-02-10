class UpdateManager:
    updateables = []

    @staticmethod
    def update(dt):
        for object in UpdateManager.updateables:
            object.update(dt)

    @staticmethod
    def add_updateable_object(updateable):
        UpdateManager.updateables.append(updateable)
