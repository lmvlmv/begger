
class Combos(object):

    def __init__(self):
        from sympy.utilities.iterables import multiset_permutations
        self.combos = list(multiset_permutations(['J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K', 'A']))

    def __call__(self):
        return self.combos
  
    