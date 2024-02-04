class Hand:
    def __init__(self):
        self.cards = []
        self.cards_limit = 10

    def add(self, card):
        if len(self.cards) >= self.cards_limit:
            self.discard(card)
        else:
            card.set_observer(self)
            self.cards.insert(0, card)

    def use(self, card):
        card.use()
        self.discard(card)

    def discard(self, card):
        self.cards.remove(card)

    def exhaust(self, card):
        pass

    def draw(self, screen):
        for card in self.cards:
            card.draw(screen)

    def calculate_new_positions():
        pass

    def update():
        pass
