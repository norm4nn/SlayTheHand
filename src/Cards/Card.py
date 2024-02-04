class Card:
    def __init__(self, rect, name, desc, image):
        self.rect = rect
        self.name = name
        self.desc = desc
        self.image = image
        self.observer = None

    def use(self):
        pass
        # TAKE SOME ACTION HERE

    def set_observer(self, observer):
        self.observer = observer

    def onclick(self):
        self.observer.use(self)
