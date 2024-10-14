from math import *


def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A


def show(sc):
    return ("\n".join(["".join(s) for s in sc][::-1]))


def F(func_name):
    def func(x):
        return eval(func_name)
    return func
    

s = input().split()
W, H, A, B = [int(s[i]) for i in range(len(s) - 1)]
f = F(s[-1])
screen = [[" "] * W for _ in range(H)]

# Найдем для функции scale (ибо теперь не только sin(x), как на семинаре)
max_func_value, min_func_value = f(A), f(A)
i = A
while i <= B:
    if f(i) > max_func_value:
          max_func_value = f(i)
    if f(i) < min_func_value:
        min_func_value = f(i)
    i += 0.1

i = 0
while i < W:
    x = scale(0, W - 1, A, B, i)
    shift = round(scale(min_func_value, max_func_value, 0, H-1, f(x)))
    if 0 <= round(i) < W and 0 <= shift < H:
        screen[shift][round(i)] = "*"
    i += 0.1

print(show(screen))