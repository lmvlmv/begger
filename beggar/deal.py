#!/usr/bin/python
#from sympy.utilities.iterables import multiset_permutations

class deal(object):
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

