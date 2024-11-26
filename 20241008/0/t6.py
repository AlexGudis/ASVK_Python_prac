from math import *

def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A

def show(sc):
    return '\n'.join("".join(s) for s in sc)

W = 40
H = 20
A, B = -6, 6
screen = [[" "] * W for _ in range(H)]

i = 0
while i < W:
    x = scale(0, W - 1, A, B, i)
    y = sin(x)
    #y = (x-13)**2+x+1
    shift = round(scale(-1, 1, 0, H-1, y))
    if round(i) < W:
        screen[shift][round(i)] = "#"
    i += 0.1

print(show(screen))