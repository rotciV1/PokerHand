class PokerHandType(object):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

    @classmethod
    def to_string(cls, handType):
        stringRepr = {
            cls.HIGH_CARD: 'High Card',
            cls.ONE_PAIR: 'One Pair',
            cls.TWO_PAIR: 'Two Pair',
            cls.THREE_OF_A_KIND: 'Three of a Kind',
            cls.STRAIGHT: 'Straight',
            cls.FLUSH: 'Flush',
            cls.FOUR_OF_A_KIND: 'Four of a Kind',
            cls.STRAIGHT_FLUSH: 'Straight Flush',
            cls.ROYAL_FLUSH: 'Royal Flush'
        }

        return stringRepr[handType]
