import sys

class Beggar(object):

    @staticmethod
    def play(hands,firstCardOnLeft=True,verbose=False):
        
        def penalty_value_of(card):
            values = {"J":1,"Q":2,"K":3,"A":4}
            return values[card]

        a,b = hands #hands are called a and b
        if not firstCardOnLeft:
            a.reverse()
            b.reverse()
        stack = "" #cards in the middle
        turns = 0
        tricks = 0
        starts = 0
        player = 1 #alternates between 1 and -1
        while a!="" and b!="": #game terminates when a or b's hands are empty
            battle_in_progress = False
            cards_to_play = 1
            while cards_to_play>0: #current player may play up to cards_to_play cards
                turns=turns+1
                
                try:
                    if player==1:
                        #grab next card from first character of string a
                        next_card = a[0] 
                        a = a[1:]
                    else:
                        #grab next card from first character of string b
                        next_card = b[0]
                        b = b[1:]
                except IndexError:
                    break #ran out of cards to play, game over...
                
                stack = stack+next_card #add to the stack
                
                if next_card=='-':
                    #not a court card
                    if battle_in_progress:
                        cards_to_play=cards_to_play-1 #this player needs keep trying to find a court card
                    else:
                        player = player*-1 #no court cards found yet, back to other player
                else:
                    #court card found, back to the other player
                    battle_in_progress = True 
                    cards_to_play = penalty_value_of(next_card)
                    player = player*-1
                    
            #end of trick, make the losing player pick up the cards in the stack
            tricks = tricks+1
            if player==1:
                b = b+stack 
                stack = ''
            else:
                a = a+stack 
                stack = ''
        
            if len(a) == len(b):
                starts += 1	
    
            player = player*-1
            
            #print current status
            if verbose:
                print "%s/%s/%s\r" % (a,b,stack)
        return (turns, tricks, starts)




class GameNo(object):
    def __init__(self, start = -1, maxgame = 4503530907893760):
        self.start = start
        self.maxgame = maxgame


    def __iter__(self):
        return self

    def next(self):
        x = 0
        while self.start < self.maxgame:
            x = bin(self.start).count('1')
            if x == 16:
                self.start += 1
                return int(self.start-1)
            else:
                self.start += 1
        raise StopIteration()    

class Deal(object):

    def __init__(self, gameno):
        from combos import Combos
        from sympy.utilities.iterables import multiset_permutations
        self._gameno = gameno 	
        # self._perm = Combos()()
        self._perm = multiset_permutations(['J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K', 'A'])
        
    def __iter__(self):	
        return self

    def next(self):
        while(self._perm):
            court = self._perm.next()
            deck = ""
            for b in format(self._gameno, '048b'):
                if b == "0":
                    deck += "-"
                else:
                    deck += court.pop()
            #sys.stdout.write("{}/{}\r".format(deck[:25],deck[26:]))
            return (deck[0:25],deck[26:51])
        raise StopIteration() 

