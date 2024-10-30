import sys


def fib(m, n):
    f_1 = 1
    f_2 = 1
    for i in range(m + n):
        if i >= m:
            yield f_2

        tmp = f_1
        f_1 += f_2
        f_2 = tmp


exec(sys.stdin.read())