x = int(input())
if x % 2 == 0 and x % 25 == 0:
    print("A +", end=' ')
else:
    print("A -", end=' ')
if x % 2 == 1 and x % 25 == 0:
    print("B +", end=' ')
else:
    print("B -", end=' ')
if x % 8 == 0:
    print("C +")
else:
    print("C -")