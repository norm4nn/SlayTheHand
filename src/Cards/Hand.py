from Engine.config import Config


class Hand:
    def __init__(self):
        self.cards = []
        self.cards_limit = 10
        self.y = Config.HEIGHT - 2 * Config.DEFAULT_CARD_HEIGHT / 3
        self.padding = Config.DEFAULT_CARD_WIDTH / 10

    def add(self, card):
        if len(self.cards) >= self.cards_limit:
            self.discard(card)
        else:
            card.set_observer(self)
            self.cards.append(card)
            self.calculate_position_for_cards()

    def use(self, card):
        card.use()
        self.discard(card)

    def discard(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def exhaust(self, card):
        pass

    def draw(self, screen):
        for card in self.cards:
            card.draw(screen)

    def calculate_position_for_cards(self):
        no_of_cards = len(self.cards)
        no_of_paddings = no_of_cards - 1
        hand_width = (
            no_of_cards * Config.DEFAULT_CARD_WIDTH + no_of_paddings * self.padding
        )
        start_from_x = (Config.WIDTH - hand_width) // 2
        for i, card in enumerate(self.cards):
            card.add_destination_xy(
                (start_from_x + i * (Config.DEFAULT_CARD_WIDTH + self.padding), self.y)
            )

    def update(self, dt):
        for card in self.cards:
            card.update(dt)
