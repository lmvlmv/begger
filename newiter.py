#!/usr/bin/python
from beggar import BeggarGame, Court, Deck, Player
import time
import sys
from tqdm import tqdm


def report(res):
    for r in res:
        print("Game {}, max {}".format(r[0], r[1]))


start = 4433230883192896

deck = Deck(court=Court().default(), decksize=52)

# c = Court()
# c.add("A", 4, 3)
# c.add("K", 3, 3)
# c.add("Q", 2, 3)
# c.add("J", 1, 3)
# deck = Deck(court=c, decksize=52)
bg = BeggarGame(deck, gamenum=start)


turns = 0
longest = 0
pbar = tqdm(total=deck.court.permutations, unit='Games', ncols=140,
        bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}] {rate_fmt} {postfix[0]} {postfix[1][maxturns]}', postfix=["Max Turns:", dict(maxturns=0)])
try:
    while True:        
        (turns, tricks, starts) = Player(deck.court.courtmap, next(bg.dealer())).play()
        if turns > longest:
            longest = turns
            pbar.postfix[1]['maxturns'] = longest
        # print (turns, tricks, starts)
        pbar.update()
except StopIteration:
    pbar.update()
    #print(longest)

