#!/usr/bin/python
from  beggar import Beggar, Deal, GameNo
import time
import sys
from tqdm import tqdm

def play(game):
    turns = 0
    deal = Deal(game)
    longest = 0 

    pbar = tqdm(total=63063000, unit='Games', ncols=140, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}] {rate_fmt} {postfix[0]} {postfix[1][maxturns]}', postfix=["Max Turns:", dict(maxturns=0)])
    for (left,right) in deal:
        (turns, tricks, starts) = Beggar.play((left,right),verbose=False) 
        if turns >  longest:
            longest = turns
            pbar.postfix[1]['maxturns'] = longest
        pbar.update()
        next(deal)
        #print "Turns: {} Tricks: {} Starts {}".format(turns, tricks, starts)


def report(res):
    for r in res:
        print "Game {}, max {}".format(r[0], r[1])

start = 4433230883192895
trials = 10
d = GameNo(start=start)
games = [ d.next() for i in range(trials) ]
for game in games:
    play(game)
# if __name__ == '__main__':  
#     from multiprocessing import Pool
#     p = Pool(4)
#     p.map_async(play, games, callback=report)
#     p.close()
#     p.join()




#try:
#    from numpy import histogram
#    (hist, bins) = histogram(turnlist, bins=50, range=(0,5000))
#    for (v,b) in zip(hist, [int(i) for i in bins]):
#        print "{0},{1}".format(b,v) 
#except ImportError:
#    print "No Numpy module"
