from itertools import *

print([f"{v}{h}" for v, h in list(product('ABCDEFGH', range(1, 9)))]) 