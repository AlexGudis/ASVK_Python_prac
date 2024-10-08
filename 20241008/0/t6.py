from math import *

def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A

def show(sc):
    return '\n'.join("".join(s) for s in sc)

W = 60
H = 20
A, B = -3, 4
screen = [[" "] * W for _ in range(H)]

for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = sin(x)
    shift = round(scale(-1, 1, 0, H-1, y))
    screen[shift][i] = "#"

print(show(screen))