from math import *

def S(f, g):
    def fun(x):
        return f(x) + g(x)
    return fun


res = S(sin, cos)
print(res(pi))