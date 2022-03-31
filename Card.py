from collections import namedtuple


class Card(namedtuple("Card", ["value", "suit"])):
    __slots__ = ()

    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    SUITS = ['S', 'H', 'D', 'C']

    RANKS = {value: index for index, value in enumerate(VALUES, start=2)}

    RANKS['AW'] = 1

    @classmethod
    def fromString(cls, cardStr):
        """
        Constroi um objeto Card a partir de uma representação string de uma carta. A string deve ser um Value (valor da carta) seguido por um Suit (naipe da carta).

        :param cardStr: uma carta codificada em string
        :type cardStr: string
        :return: uma carta
        :rtype: Card
        """
        if len(cardStr) != 2 or cardStr[0] not in cls.VALUES or cardStr[1] not in cls.SUITS:
            raise ValueError(
                'Invalid string value for card \n Valor string invalido para carta')
        return cls(cardStr[0], cardStr[1])

    def __str__(self):
        return '{}{}'.format(self.value, self.suit)

    __repr__ = __str__
