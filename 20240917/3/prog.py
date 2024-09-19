n = int(input())
i = 0
while i < 3:
    j = 0
    while j < 3:
        x = (n + i) * (n + j)
        tmp = x
        summ = 0
        while tmp != 0:
            summ += tmp % 10
            tmp //= 10
        if summ == 6:
            x = ':=)'
        print( n + i, '*', n + j, '=', x, end=' ')
        j += 1
    i += 1
    print()