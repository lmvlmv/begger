import sys


class Beggar(object):

    @staticmethod
    def play(hands, firstCardOnLeft=True, verbose=False):

        def penalty_value_of(card):
            values = {"J": 1, "Q": 2, "K": 3, "A": 4}
            return values[card]

        a, b = hands  # hands are called a and b
        if not firstCardOnLeft:
            a.reverse()
            b.reverse()
        stack = ""  # cards in the middle
        turns = 0
        tricks = 0
        starts = 0
        player = 1  # alternates between 1 and -1
        while a != "" and b != "":  # game terminates when a or b's hands are empty
            battle_in_progress = False
            cards_to_play = 1
            while cards_to_play > 0:  # current player may play up to cards_to_play cards
                # print current status
                if verbose:
                    print(("%s/%s/%s\r" % (a, b, stack)))
                turns = turns+1

                try:
                    if player == 1:
                        # grab next card from first character of string a
                        next_card = a[0]
                        a = a[1:]
                    else:
                        # grab next card from first character of string b
                        next_card = b[0]
                        b = b[1:]
                except IndexError:
                    break  # ran out of cards to play, game over...

                stack = stack+next_card  # add to the stack

                if next_card == '-':
                    # not a court card
                    if battle_in_progress:
                        # this player needs keep trying to find a court card
                        cards_to_play = cards_to_play-1
                    else:
                        player = player*-1  # no court cards found yet, back to other player
                else:
                    # court card found, back to the other player
                    battle_in_progress = True
                    cards_to_play = penalty_value_of(next_card)
                    player = player*-1

            # end of trick, make the losing player pick up the cards in the stack
            tricks = tricks+1
            if player == 1:
                b = b+stack
                stack = ''
            else:
                a = a+stack
                stack = ''

            if len(a) == len(b):
                starts += 1

            player = player*-1

        return (turns, tricks, starts)


class Court(object):

    def __init__(self):
        self.__courtmap = {}

    def add(self, label, value, count):

        import string
        # check label is single character
        if label not in list(string.ascii_uppercase):
            raise ValueError(
                "Label for court card must be single character between A-Z")

        # check value is int
        if not isinstance(value, int):
            raise TypeError("value must be an int")

        if (value < 0) or (value > 9):
            raise ValueError("value must be positive between 1 and 9")

        self.__courtmap.update({label: {'value': value, 'count': count}})

    def addcourt(self):
        # maybe add whole court in one go
        pass

    def default(self):
        c = Court()
        c.add("A", 4, 4)
        c.add("K", 3, 4)
        c.add("Q", 2, 4)
        c.add("J", 1, 4)
        return c

    def courtcards(self):
        import itertools
        c = []
        for x in self.__courtmap.keys():
            c.append(list(x * self.__courtmap[x]['count']))
        return list(itertools.chain.from_iterable(c))

    def permute(self):
        from sympy.utilities.iterables import multiset_permutations
        return multiset_permutations(self.courtcards())

    @property
    def courtcount(self):
        return len(self.courtcards())

    @property
    def permutations(self):
        from math import factorial
        from functools import reduce
        # return sum(1 for x in self.permute())
        # X total elements. N different elements with count N1 N2 N3 etc
        # permutations =  X!/(N1! * N2! * N3! ...)
        # NOTE requires // operation to avoid float
        return (factorial(self.courtcount))//(reduce(lambda x, y: x*y, [factorial(self.__courtmap[x]['count']) for x in self.__courtmap.keys()]))


class BeggarGame(object):

    def __init__(self, court=None, decksize=52):
        self.__court = court or Court().default()
        self.__fullcourt = self.__court.courtcards()

        if not isinstance(self.__court, Court):
            raise TypeError("Pass a Court object")

        if decksize % 2:
            raise ValueError("Deck must be even")

        if decksize < len(self.__court.courtcards()):
            raise ValueError(
                "Deck size must be at least equal to number of court cards")

        self.__decksize = decksize

    def Create(self):
        return BeggarGame()

    class GameNo(object):
        def __init__(self, courtcount, decksize):
            self.__courtcount = courtcount
            self.__decksize = decksize

            if courtcount > decksize:
                raise ValueError("Deck must be >= court count")
            
            self.__mingame = int('1' * self.__courtcount, 2)
            self.__maxgame = int(('1' * self.__courtcount) + ('0' * (self.__decksize - self.__courtcount)), 2)
            self.__currentgame = self.__mingame

        def __iter__(self):
            return self

        def __next__(self):
            x = 0
            while self.__currentgame <= self.__maxgame:
                x = bin(self.__currentgame).count('1')
                if x == self.__courtcount:
                    self.__currentgame += 1
                    return int(self.__currentgame-1)
                else:
                    self.__currentgame += 1
            raise StopIteration()

    @property
    def totalgames(self):
        from math import factorial
        # NOTE requires // division operator to avoid float conversion
        return (factorial(self.__decksize)//factorial(self.__court.courtcount)) * self.__court.permutations

    @property
    def deck(self):
        cards = []
        fc = self.__fullcourt[:]
        for b in format(self.perm_id, '0{}b'.format(self.__cards)):
            if b == "0":
                cards += "-"
            else:
                cards += fc.pop()
        return ''.join(cards)

    @deck.setter
    def deck(self, deck):
        pass

    @property
    def hands(self):
        return (self.deck[:(self.__cards/2)], self.deck[(self.__cards/2):])

    @property
    def perm_id(self):
        if self.__perm_id:
            return self.__perm_id
        raise AttributeError

    @perm_id.setter
    def perm_id(self, g):
        if self.validate_perm_id(g):
            self.__perm_id = g
        else:
            raise ValueError

    @property
    def courtorder(self):
        if self.__courtorder:
            return self.__courtorder
        raise AttributeError

    @courtorder.setter
    def courtorder(self, c):
        if self.validate_courtorder(c):
            self.__courtorder = c
        else:
            raise ValueError

    def validate_courtorder(self, c):
        if not isinstance(c, str):
            raise TypeError

        if sorted(self.__fullcourt) == sorted(c):
            return True
        return False

    def validate_perm_id(self, g):
        if self.bitcount(g) == len(self.__fullcourt):
            return True
        return False

    @staticmethod
    def bitpattern(n, l):
        return format(n, '0{}b'.format(l))

    @staticmethod
    def bitcount(n):
        return format(n, 'b').count('1')

    def validate_hands(self, l, r):
        if (len(l) != len(r) != self.__cards/2):
            print(("Wrong hand sizes {} {}".format(len(l), len(r))))
            raise ValueError

        for court in self.__courtcards:
            if (l+r).count(court) != len(self.__fullcourt):
                print(("Wrong number of {}: {}".format(court, (l+r).count(court))))
                raise ValueError


class GameNo(object):
    def __init__(self, start=-1, maxgame=4503530907893760):
        self.start = start
        self.maxgame = maxgame

    def __iter__(self):
        return self

    def __next__(self):
        x = 0
        while self.start < self.maxgame:
            x = bin(self.start).count('1')
            if x == 16:
                self.start += 1
                return int(self.start-1)
            else:
                self.start += 1
        raise StopIteration()


class Deal(object):

    def __init__(self, gameno):
        from .combos import Combos
        from sympy.utilities.iterables import multiset_permutations
        self._gameno = gameno
        # self._perm = Combos()()
        self._perm = multiset_permutations(
            ['J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A'])

    def __iter__(self):
        return self

    def __next__(self):
        while(True):
            try:
                court = next(self._perm)
            except StopIteration:
                raise
            deck = ""
            for b in format(self._gameno, '052b'):
                if b == "0":
                    deck += "-"
                else:
                    deck += court.pop()
            # try:
            #     BeggarGame().validate_hands(deck[:26], deck[26:])
            # except Exception as ex:
            #     print(ex)
            #     sys.exit(1)
            return (deck[:26], deck[26:])
        raise StopIteration()
