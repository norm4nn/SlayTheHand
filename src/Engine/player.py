from Cards.Hand import Hand
from Cards.Card import Card


class Player:
    hand = Hand()

    @staticmethod
    def add_card():
        card = Card.generateCard()
        Player.hand.add(card)
