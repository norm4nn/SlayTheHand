from Engine.config import Config


class Hand:
    def __init__(self):
        self.cards = []
        self.cards_limit = 10
        self.y = Config.HEIGHT - 6 * Config.DEFAULT_CARD_HEIGHT / 7
        self.padding = 2
        self.max_angle = 15
        self.drawing_order = []
        self.currently_hovered = None

    def add(self, card):
        if len(self.cards) >= self.cards_limit:
            self.discard(card)
        else:
            card.set_observer(self)
            self.cards.append(card)
            self.drawing_order.append(card)
            self.calculate_position_for_cards()

    def use(self, card):
        card.use()
        self.discard(card)

    def discard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            self.drawing_order.remove(card)

    def exhaust(self, card):
        pass

    def draw(self, screen):
        for card in self.drawing_order:
            card.draw(screen)

    def calculate_position_for_cards(self):
        self.drawing_order = self.cards.copy()
        no_of_cards = len(self.cards)
        mid_points = (no_of_cards // 2, (no_of_cards - 1) // 2)

        for i, card in enumerate(self.cards):
            x = self.get_default_x(card)
            y = self.get_default_y(card)
            card.add_destination_xy((x, y))
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

    def hovered_card(self, card):
        if self.currently_hovered is None:
            card.xy = self.get_default_x(card), self.get_default_y(card)
            card.hover()
            self.drawing_order.remove(card)
            self.drawing_order.append(card)
            self.currently_hovered = card
            card_found = False
            move_by = Config.DEFAULT_CARD_WIDTH // 2
            for other_card in self.cards:
                y = self.get_default_y(other_card)
                x = self.get_default_x(other_card)
                if other_card == card:
                    card_found = True
                    continue
                if not card_found:
                    other_card.add_destination_xy((x - move_by, y))
                else:
                    other_card.add_destination_xy((x + move_by, y))

    def unhovered_card(self, card):
        if self.currently_hovered is card:
            card.unhover()
            self.currently_hovered = None
            self.calculate_position_for_cards()

    def get_default_y(self, card):
        i = self.cards.index(card)
        no_of_cards = len(self.cards)
        mid_points = (no_of_cards // 2, (no_of_cards - 1) // 2)
        d = self.calc_distance_from_mid(mid_points, i)
        return self.y + d * d * self.padding

    def get_default_x(self, card):
        i = self.cards.index(card)
        no_of_cards = len(self.cards)
        hand_width = Config.DEFAULT_CARD_WIDTH * (no_of_cards - (no_of_cards - 1) / 3)
        start_from_x = (Config.WIDTH - hand_width) // 2
        return start_from_x + i * (2 * Config.DEFAULT_CARD_WIDTH / 3)
