from Engine.config import Config


class Hand:
    def __init__(self):
        self.cards = []
        self.cards_limit = 10
        self.y = Config.HEIGHT - 6 * Config.DEFAULT_CARD_HEIGHT / 7
        self.padding = Config.DEFAULT_CARD_WIDTH / 20
        self.max_angle = 15

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
        mid_points = (no_of_cards // 2, (no_of_cards - 1) // 2)
        hand_width = (
            no_of_cards * Config.DEFAULT_CARD_WIDTH + no_of_paddings * self.padding
        )

        start_from_x = (Config.WIDTH - hand_width) // 2
        for i, card in enumerate(self.cards):
            d = self.calc_distance_from_mid(mid_points, i)
            card.add_destination_xy(
                (
                    start_from_x + i * (Config.DEFAULT_CARD_WIDTH + self.padding),
                    self.y + d * d * self.padding,
                )
            )
            angle = self.calc_angle(i, mid_points)
            card.rotate_to(angle)

    def update(self, dt):
        for card in self.cards:
            card.update(dt)

    def calc_distance_from_mid(self, mid_points, i):
        p1, p2 = mid_points
        return min(abs(p1 - i), abs(p2 - i))

    def calc_angle(self, i, mid_points):
        sign = 0
        if i < mid_points[0]:
            sign = 1
        if i > mid_points[1]:
            sign = -1

        d = self.calc_distance_from_mid(mid_points, i)

        return d * sign * self.max_angle / ((self.cards_limit - 1) // 2)
