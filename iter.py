0#!/usr/bin/python
import beggar
import time
import sys

def play(game):
    turns = 0
    cont = True
    print ".",
    deal = beggar.Deal(game)
    stats = [] 
    while(cont):
        try:
            (left, right) = deal.next()
            (turns, tricks, starts) = beggar.play((left,right),verbose=False) 
            stats.append(turns)
            #print "Turns: {} Tricks: {} Starts {}".format(turns, tricks, starts)
        except StopIteration:
            cont = False
    return (game, max(stats))  


def report(res):
    for r in res:
        print "Game {}, max {}".format(r[0], r[1])

start = 4433230883192895
trials = 100
d = beggar.GameNo(start=start)
games = [ d.next() for i in range(trials) ]
# for game in games:
#     play(game)
if __name__ == '__main__':  
    from multiprocessing import Pool
    p = Pool(4)
    p.map_async(play, games, callback=report)
    p.close()
    p.join()




#try:
#    from numpy import histogram
#    (hist, bins) = histogram(turnlist, bins=50, range=(0,5000))
#    for (v,b) in zip(hist, [int(i) for i in bins]):
#        print "{0},{1}".format(b,v) 
#except ImportError:
#    print "No Numpy module"
