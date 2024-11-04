from itertools import *

def slide(seq, n):
    ind = 0
    for i in tee(seq, len(seq)): 
        check = islice(i, ind, n + ind)
        # print(check)
        yield from check
        ind += 1

import sys
exec(sys.stdin.read())