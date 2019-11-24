#!/usr/bin/python
from beggar import BeggarGame, Court, Deck
import time
import sys,os
from tqdm import tqdm


def report(res):
    for r in res:
        print("Game {}, max {}".format(r[0], r[1]))


start = 4433230883192896

start = 0 
deck = Deck(court=Court().default(), decksize=52)

# c = Court()
# c.add("A", 4, 4)
# c.add("K", 3, 3)
# c.add("Q", 2, 3)
# c.add("J", 1, 3)
# deck = Deck(court=c, decksize=52)
bg = BeggarGame(deck, gamenum=start)

os.environ['BROKER_POOL_LIMIT'] = 'None'
from celery import Celery
from beggarplay import play as celplay
app = Celery('celiter', backend='rpc://', broker='pyamqp://')

turns = 0
longest = 0

from iteration_utilities import grouper

b = grouper(bg.dealer(), 100000)

try:
    while True:
        for chunk in tqdm(iterable=b, total=deck.court.permutations//100000, unit='chunks'):
            res = celplay.chunks([ (deck.court.courtmap, x) for x in chunk ], 100)()
            res.get()
except StopIteration:
    pass


# pbar = tqdm(total=deck.court.permutations, unit='Games', ncols=140,
#         bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}] {rate_fmt} {postfix[0]} {postfix[1][maxturns]}', postfix=["Max Turns:", dict(maxturns=0)])
# try:
#     while True:  
#         res = celplay.delay(deck.court.courtmap, bg.deal())
#         (turns, tricks, starts) = res.get()
#         if turns > longest:
#             longest = turns
#             pbar.postfix[1]['maxturns'] = longest
#         # print (turns, tricks, starts)
#         pbar.update()
# except StopIteration:
#     pbar.update()
#     print(longest)
