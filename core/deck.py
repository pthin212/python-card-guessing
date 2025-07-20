import random

SUITES = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['A'] + list(map(str, range(2, 11))) + ['J', 'Q', 'K']
JOKERS = ['Red Joker', 'Black Joker']

RANK_ORDER = {rank: i for i, rank in enumerate(RANKS, start=1)}
SUITE_ORDER = {suite: i for i, suite in enumerate(SUITES, start=1)}
JOKER_ORDER = {'Red Joker': 100, 'Black Joker': 99}

class Card:
    def __init__(self, rank, suite=None):
        self.rank = rank
        self.suite = suite

    def __str__(self):
        return f"{self.rank} of {self.suite}" if self.suite else self.rank

    @property
    def value(self):
        if self.rank in JOKER_ORDER:
            return JOKER_ORDER[self.rank]
        return RANK_ORDER[self.rank] + (SUITE_ORDER[self.suite] * 0.1)

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suite) for suite in SUITES for rank in RANKS]
        self.cards += [Card(joker) for joker in JOKERS]
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self.__init__()
        return self.cards.pop()
