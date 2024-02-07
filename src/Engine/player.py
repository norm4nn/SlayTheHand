from Cards.generateCard import generateCard
from Cards.Hand import Hand


class Player:
    hand = Hand()

    @staticmethod
    def add_card():
        card = generateCard()
        Player.hand.add(card)
