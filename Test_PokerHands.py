import unittest

from PokerHand import Pokerhand, PokerHandType


class TestPokerHand(unittest.TestCase):
    def test_StringRepresentation(self):
        self.assertEqual('{}'.format(Pokerhand.fromString(
            'KD QH 8C 9H 5S')), "<hand [KD, QH, 8C, 9H, 5S], 'High Card'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            'KH 5D KD 7H 8D')), "<hand [KH, 5D, KD, 7H, 8D], 'One Pair'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            '2D 2S 6D 4H 4D')), "<hand [2D, 2S, 6D, 4H, 4D], 'Two Pair'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            '4D AC AD AH 8D')), "<hand [4D, AC, AD, AH, 8D], 'Three of a Kind'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            "4D 5D 6D 7H 8D")), "<hand [4D, 5D, 6D, 7H, 8D], 'Straight'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            "2D 3D 7D QD AD")), "<hand [2D, 3D, 7D, QD, AD], 'Flush'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            '5H 5C QD QC QS')), "<hand [5H, 5C, QD, QC, QS], 'Full House'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            "7S TC TH TS TD")), "<hand [7S, TC, TH, TS, TD], 'Four of a Kind'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            '5S 6S 7S 8S 9S')), "<hand [5S, 6S, 7S, 8S, 9S], 'Straight Flush'>")
        self.assertEqual('{}'.format(Pokerhand.fromString(
            'TS JS QS KS AS')), "<hand [TS, JS, QS, KS, AS], 'Royal Flush'>")

    def test_SortingByHandType(self):
        h1 = Pokerhand.fromString('KD QH 8C 9H 5S')
        h2 = Pokerhand.fromString('KH 5D KD 7H 8D')
        h3 = Pokerhand.fromString('2D 2S 6D 4H 4D')
        h4 = Pokerhand.fromString('4D AC AD AH 8D')
        h5 = Pokerhand.fromString('4D 5D 6D 7H 8D')
        h6 = Pokerhand.fromString('2D 3D 7D QD AD')
        h7 = Pokerhand.fromString('5H 5C QD QC QS')
        h8 = Pokerhand.fromString('7S TC TH TS TD')
        h9 = Pokerhand.fromString('5S 6S 7S 8S 9S')
        h10 = Pokerhand.fromString('TS JS QS KS AS')
        hands = [h5, h2, h7, h8, h1, h4, h10, h6, h3, h9]
        sortedHands = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]
        self.assertEqual(sorted(hands), sortedHands)

    def test_HighCard(self):
        h1 = Pokerhand.fromString('KH QH 2C 5D 8D')
        h2 = Pokerhand.fromString('KD QH 8C 2H 5S')
        h3 = Pokerhand.fromString('QD TS 8H 9D 7S')
        self.assertEqual(h1.handType, PokerHandType.HIGH_CARD)
        self.assertEqual(h2.handType, PokerHandType.HIGH_CARD)
        self.assertTrue(h3.handType == PokerHandType.HIGH_CARD)
        self.assertTrue(h1 == h2)
        self.assertTrue(h1 > h3)

    def test_OnePair(self):
        h1 = Pokerhand.fromString('KH KS JC JD 8D')
        h2 = Pokerhand.fromString('KD KC 8C JH JS')
        h3 = Pokerhand.fromString('8D 8S 5H 5S AS')
        h4 = Pokerhand.fromString('QD QS JH JS 8S')
        self.assertEqual(h1.handType, PokerHandType.TWO_PAIR)
        self.assertEqual(h2.handType, PokerHandType.TWO_PAIR)
        self.assertEqual(h3.handType, PokerHandType.TWO_PAIR)
        self.assertEqual(h4.handType, PokerHandType.TWO_PAIR)
        self.assertTrue(h1 == h2)
        self.assertTrue(h1 > h3)
        self.assertTrue(h1 > h4)

    def test_ThreeOfAKind(self):
        h1 = Pokerhand.fromString('JH QH JC JD 8D')
        h2 = Pokerhand.fromString('JD QH 8C JH JS')
        h3 = Pokerhand.fromString('AD KS TH TD TS')
        self.assertEqual(h1.handType, PokerHandType.THREE_OF_A_KIND)
        self.assertEqual(h2.handType, PokerHandType.THREE_OF_A_KIND)
        self.assertEqual(h3.handType, PokerHandType.THREE_OF_A_KIND)
        self.assertTrue(h1 == h2)
        self.assertTrue(h1 > h3)

    def test_Straight(self):
        h1 = Pokerhand.fromString('4H 5H 6C 7D 8D')
        h2 = Pokerhand.fromString('4D 5S 6D 7H 8S')
        h3 = Pokerhand.fromString('3D 4S 5H 6D 7S')
        h4 = Pokerhand.fromString('AD 3S 5H 2D 4S')
        self.assertEqual(h1.handType, PokerHandType.STRAIGHT)
        self.assertEqual(h2.handType, PokerHandType.STRAIGHT)
        self.assertEqual(h3.handType, PokerHandType.STRAIGHT)
        self.assertEqual(h4.handType, PokerHandType.STRAIGHT)
        self.assertTrue(h1 == h2)
        self.assertTrue(h1 > h3)
        self.assertTrue(h1 > h4)

    def test_Flush(self):
        h1 = Pokerhand.fromString('KH AH TH 5H 8H')
        h2 = Pokerhand.fromString('KS AS TS 8S 5S')
        h3 = Pokerhand.fromString('KH AH 3H 5H 8H')
        self.assertEqual(h1.handType, PokerHandType.FLUSH)
        self.assertEqual(h2.handType, PokerHandType.FLUSH)
        self.assertEqual(h3.handType, PokerHandType.FLUSH)
        self.assertTrue(h1 == h2)
        self.assertTrue(h1 > h3)

    def test_FullHouse(self):
        h1 = Pokerhand.fromString('KH KC KS QD QC')
        h2 = Pokerhand.fromString('QD QS QH AD AS')
        self.assertEqual(h1.handType, PokerHandType.FULL_HOUSE)
        self.assertEqual(h2.handType, PokerHandType.FULL_HOUSE)
        self.assertTrue(h1 > h2)

    def test_StraightFlush(self):
        h1 = Pokerhand.fromString('KH KC KS KD 2C')
        h2 = Pokerhand.fromString('QD QS QH QC AS')
        self.assertEqual(h1.handType, PokerHandType.FOUR_OF_A_KIND)
        self.assertEqual(h2.handType, PokerHandType.FOUR_OF_A_KIND)
        self.assertTrue(h1 > h2)

    def test_StraightFlush(self):
        h1 = Pokerhand.fromString('8H 9H TH JH QH')
        h2 = Pokerhand.fromString('QS JS TS 9S 8S')
        h3 = Pokerhand.fromString('9D TD JD QD KD')
        self.assertEqual(h1.handType, PokerHandType.STRAIGHT_FLUSH)
        self.assertEqual(h2.handType, PokerHandType.STRAIGHT_FLUSH)
        self.assertEqual(h3.handType, PokerHandType.STRAIGHT_FLUSH)
        self.assertTrue(h1 == h2)
        self.assertTrue(h1 < h3)

    def test_RoyalFlush(self):
        h1 = Pokerhand.fromString('TD JD QD KD AD')
        h2 = Pokerhand.fromString('TH JH QH KH AH')
        self.assertEqual(h1.handType, PokerHandType.ROYAL_FLUSH)
        self.assertEqual(h2.handType, PokerHandType.ROYAL_FLUSH)
        self.assertNotEqual(h1.handType, PokerHandType.STRAIGHT_FLUSH)
        self.assertTrue(h1 == h2)

    if __name__ == '__main__':
        unittest.main()
