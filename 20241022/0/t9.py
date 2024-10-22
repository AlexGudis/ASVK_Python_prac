from itertools import *

def ffn(n, seq):
    return filterfalse(lambda x: x % n, seq)

print(list(ffn(7, range(10, 66))))