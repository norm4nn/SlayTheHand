from Cards.generateCard import generateCard
from Cards.Hand import Hand


class Engine:
    hand = Hand()

    @staticmethod
    def add_card():
        card = generateCard()
        Engine.hand.add(card)
