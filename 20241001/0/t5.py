from math import *

def MINF(*args):
    def g(x):
        return min([el(x) for el in args])
    return g

f = MINF(sin, cos, tan, atan)
print(f(pi/4))