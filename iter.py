#!/usr/bin/python
import beggarmypython
from sympy.utilities.iterables import multiset_permutations
import time
import sys

class deal():
    def __init__(self, start = -1, max = 2251250057871360):
        self.start = start
        self.max = max

    def __iter__(self):
        return self

    def next(self):
        x = 0
        if self.start < self.max:
            while( x != 12):
                self.start += 1
                x = bin(self.start).count('1')
            return int(self.start)            
        else:
            raise StopIteration()    

deal = deal(start = 42153421543)
d = 0
trials = 10
max = 0
turnlist = []
while(trials > 0):
    d = deal.next()
    print d
    trials -= 1
    a = multiset_permutations(['J','Q','K','J','Q','K','J','Q','K','J','Q','K']) 
    count = 0
    turns = 0
    cont = True
    while(cont):
        try:
            count = count + 1
            r = a .next()
            s = ""
            for c in format(d, '048b'):
                if c == "0":
                    s += "-"
                else:
                    s += r.pop()

                        
            left = s[0:25]
            right = s[26:51]
            #print "Starting hands: {0}/{1}".format(left, right)
            turns = beggarmypython.play((left,right),verbose=False)
            sys.stdout.write("\rMax turns: {0}\tPlayed: {1:05}\t Game: {2}/{3}".format(max, count, left, right))
            sys.stdout.flush()
            turnlist.append(turns)
            if (turns >  max):
                max = turns
                print "\nMax turns found on game: {0}/{1}".format(left, right)
        except StopIteration:
            cont = False
    print "Next? {}".format(trials)

try:
    from numpy import histogram
    (hist, bins) = histogram(turnlist, bins=50, range=(0,5000))
    for (v,b) in zip(hist, [int(i) for i in bins]):
        print "{0},{1}".format(b,v) 
except ImportError:
    print "No Numpy module"
