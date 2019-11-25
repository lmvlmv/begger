#!/usr/bin/python
from iteration_utilities import grouper
from beggarplay import play as celplay
from celery import Celery
from beggar import BeggarGame, Court, Deck
import time
import sys
import os
from tqdm import tqdm


def report(res):
    for r in res:
        print("Game {}, max {}".format(r[0], r[1]))


start = 4433230883192896

# start = 0
deck = Deck(court=Court().default(), decksize=52)

# c = Court()
# c.add("A", 4, 4)
# c.add("K", 3, 3)
# c.add("Q", 2, 3)
# c.add("J", 1, 3)
# deck = Deck(court=c, decksize=52)
bg = BeggarGame(deck, gamenum=start)

os.environ['BROKER_POOL_LIMIT'] = 'None'
app = Celery('celiter', backend='rpc://', broker=os.environ['BROKERURL'])


longest = 0

handchunk = 10000
taskchunk = 1000
rescollect = 100

b = grouper(bg.dealer(), handchunk)
res = []
results = []
try:
    while True:
        pbar = tqdm(total=deck.court.permutations,
                    unit=' hands',
                    ncols=140,
                    bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}] {rate_fmt} {postfix[0]} {postfix[1][maxturns]}',
                    postfix=["Max Turns:", dict(maxturns=0)])
        for chunk in b:
            res.append(celplay.chunks(
                [(deck.court.courtmap, x) for x in chunk], taskchunk)())
            if len(res) == rescollect:
                for r in res:
                    for x in r.results:
                        for f in x.get():
                            results.append(f)
                chunkmax = max([t[0] for t in results])
                if chunkmax > longest:
                    longest = chunkmax
                    pbar.postfix[1]['maxturns'] = longest
                res = []
                pbar.update(handchunk*rescollect)
except StopIteration:
    for r in res:
        print("Getting result {}".format(r))
        for x in r.results:
            for f in x.get():
                results.append(f)
    print("Games: {}, Max Turns: {}".format(
        len(results), max([t[0] for t in results])))
except KeyboardInterrupt:
    for r in res:
        r.forget()


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
