from decimal import Decimal

def esum(N, one):
    summ = one
    check = one
    for i in range(2, N):
        summ += (one / check)
        check *= i
    return summ

print(esum(100, 1.0))