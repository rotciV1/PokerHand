from Card import *
from PokerhandType import PokerHandType


class Pokerhand(object):

    def __init__(self, cards):
        """
        Constroi um objeto do tipo Poker Hand de uma lista de 5 objetos tipo Card

        :param cards: 5 cartas de uma mão de poker
        :type cards: [Card, ]
        """
        if not all(isinstance(card, Card) for card in cards):
            raise ValueError(
                'invalid type for cards \n tipo invalido para cartas')

        if len(cards) != 5:
            raise ValueError(
                'Length of the hand must be 5 \n a mão deve ter 5 cartas')

        self.cards = cards
        self.handType, self.rankCounts = self._getHandDetails()

    @classmethod
    def fromString(cls, handStr):
        """
        Constroi um objeto Poker Hand a partir de uma lista de 5 cartas representadas numa string, seperado por um espaço.
        Cada carta é representada por uma letra ou numero Value e uma letra Suit.
        Values possiveis: 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A (Two, Three, ... , Ten, Jack, Queen, King, Ace)
        Suits possiveis: C, D, H, S(Clubs, Diamonds, Hearts, Spades)
        Exemplo handStr:  '4D 6H TS JS AC'

        :param handStr: Uma mão de 5 cartas codadas em uma string
        :type handStr: string
        :return: um objeto Poker Hand
        :rtype: PokerHand
        """
        cards = list(
            map(lambda cardStr: Card.fromString(cardStr), handStr.split()))
        return cls(cards)

    @staticmethod
    def _getStortedRankCounts_(rankCounts):
        """
        Define e desempacota ranks e counts dado uma associação ranksCounts. São ordenados de forma decrescente
        por count, e se count é igual, então será por rank. Sequencias de ranks e counts retornadas mantem a implicidade
        da associação para manter a ordem

        :param ranksCounts: dict com {ranks: counts}
        :type ranksCounts: dict
        :return ranks e counts ordenados e desempacotados
        :rtype: ((int, ), (int, ))
        """
        rankCountsSorted = sorted(
            rankCounts.items(), key=lambda rankCount: rankCount[0], reverse=True)
        rankCountsSorted = sorted(
            rankCountsSorted, key=lambda rankCount: rankCount[1], reverse=True)

        return zip(*rankCountsSorted)

    def _getHandDetails(self):
        """
        Retorna o tipo da mão de poker e seus ranks & counts (frequencia de cada valor na mão associado com
        uma das Card.RANKS).
        :return: uma 2-tupla: tipo de mão, ranks counts
        :rtype: (PokerHandType(Enum), dict)
        """
        allValues = [c.value for c in self.cards]
        rankCounts = {Card.RANKS[value]: allValues.count(
            value) for value, suit in self.cards}

        wheelRankCounts = {
            Card.RANKS['A']: 1,
            Card.RANKS['5']: 1,
            Card.RANKS['4']: 1,
            Card.RANKS['3']: 1,
            Card.RANKS['2']: 1
        }

        if rankCounts == wheelRankCounts:
            rankCounts[Card.RANKS['AW']] = 1
            del rankCounts[Card.RANKS['A']]

        ranks, counts = self._getStortedRankCounts_(rankCounts)

        if len(counts) < 5:
            if counts[0] == 4:
                return PokerHandType.FOUR_OF_A_KIND, rankCounts
            elif counts[0] == 3 and counts[1] == 2:
                return PokerHandType.FULL_HOUSE, rankCounts
            elif counts[0] == 3 and counts[1] == 1:
                return PokerHandType.THREE_OF_A_KIND, rankCounts
            elif counts[0] == 2 and counts[1] == 2:
                return PokerHandType.TWO_PAIR, rankCounts

            return PokerHandType.ONE_PAIR, rankCounts
        else:
            allSuits = [c.suit for c in self.cards]

            isFlush = all(s == allSuits[0] for s in allSuits[1:])

            isStraight = ranks[0] - ranks[4] == 4

            if isFlush and isStraight:
                if ranks[0] == Card.RANKS['A'] and ranks[1] == Card.RANKS['K']:
                    return PokerHandType.ROYAL_FLUSH, rankCounts
                return PokerHandType.STRAIGHT_FLUSH, rankCounts

            if isFlush:
                return PokerHandType.FLUSH, rankCounts

            if isStraight:
                return PokerHandType.STRAIGHT, rankCounts

            return PokerHandType.HIGH_CARD, rankCounts

    def __cmp__(self, other):
        if self.handType != other.handType:
            return self.handType - other.handType

        selfRanks, _ = self._getStortedRankCounts_(self.rankCounts)
        otherRanks, _ = self._getStortedRankCounts_(other.rankCounts)
        for selfRank, otherRank in zip(selfRanks, otherRanks):
            if selfRank != otherRank:
                return selfRank - otherRank

        return 0

    def __str__(self):
        return "<hand {}, '{}'>".format(self.cards, PokerHandType.to_string(self.handType))
