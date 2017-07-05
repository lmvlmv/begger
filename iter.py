#!/usr/bin/python
import beggar
import time
import sys


start = 142153421643
trials = 100
max = 0
d = beggar.GameNo(start=start)

while(trials > 0):
    trials -= 1
    turns = 0
    cont = True
    game = d.next()
    deal = beggar.Deal(game)
    while(cont):
        try:
			(left, right) = deal.next()
			(turns, tricks, starts) = beggar.play((left,right),verbose=False)
#			print "Turns: {} Tricks: {} Starts {}".format(turns, tricks, starts)
        except StopIteration:
			cont = False


def 

#try:
#    from numpy import histogram
#    (hist, bins) = histogram(turnlist, bins=50, range=(0,5000))
#    for (v,b) in zip(hist, [int(i) for i in bins]):
#        print "{0},{1}".format(b,v) 
#except ImportError:
#    print "No Numpy module"
