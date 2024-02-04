from Cards.generateCard import generateCard
from Cards.Hand import Hand


def init():
    hand = Hand()
    for _ in range(1, 2):
        card = generateCard()
        hand.add(card)

    return hand
