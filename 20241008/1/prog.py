from fractions import Fraction

def count_part(X, s):
    ans = 0
    for i in range(len(X)):
        ans += X[i] * s ** (len(X) - i - 1)
    return ans

def inp_part():
    X_n = int(inp[0])
    inp.pop(0)

    X = [0] * (X_n + 1)
    for i in range(X_n + 1):
        X[i] = Fraction(inp[0])
        inp.pop(0)
    return X



inp = input().split(', ')
s,w = Fraction(inp[0]), Fraction(inp[1])
inp.pop(0)
inp.pop(0)

A = inp_part()
#print(A)
B = inp_part()
#print(B)

up = count_part(A, s)
down = count_part(B, s)

if down == 0:
    print(False)
elif Fraction(up, down) == Fraction(w):
    print(True)
else:
    print(False)
