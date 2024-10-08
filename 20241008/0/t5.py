from math import *

def scale(a, b, A, B, x):
    x = (B - A) * (x - a) / (b - a) + A


W = 140
H = 150
A, B = -5, 5

for i in range(H):
    x = scale(0, H - 1, A, B, i)
    y = sin(x)
    shift = round((y + 1) / 2  * W)

    print(" " * shift, '*')

