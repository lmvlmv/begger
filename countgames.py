import beggar, sys
from tqdm import tqdm
count=0
gap = 0
game = 0
bigno = 4503530907893760
i = beggar.GameNo(start=1, maxgame=4294901760)

try:
    for game in tqdm(iterable=i, total=4294901760):
        count+=1   
except StopIteration:
    print ("Total games: {}".format(count))