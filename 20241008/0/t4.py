from math import *

W = 140
H = 150
A, B = -5, 5

for i in range(H):
    x = (B - A) / (H - 1) * i + A
    y = sin(x)
    shift = round((y + 1) / 2  * W)

    print(" " * shift, '*')

