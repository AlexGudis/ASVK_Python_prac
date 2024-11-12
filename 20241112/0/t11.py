from math import inf

def divisor(a, b, exp):
    if b < exp:
        raise OverflowError
    c = a / b
    return -c

def proxy(fun, *args):
    try:
        return fun(*args)
    except OverflowError as to_low:
        return "Too small to devide"

    except ZeroDivisionError:
        return inf

for i in range(-2, 3):
    print(proxy(divisor, 100, i, 1))