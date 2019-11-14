import beggar, sys
from tqdm import tqdm
count=0
gap = 0
game = 0
i = beggar.GameNo(start=1)

try:
    for game in tqdm(iterable=i, total=4503530907893760):
        pass      
except StopIteration:
    print ("Total games: {}".format(count))