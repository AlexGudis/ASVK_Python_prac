def rbin(cur, n):
    if n == 0:
        print(*cur, sep='')
    else:
        rbin(cur + [1], n - 1)
        rbin(cur + [0], n - 1)

rbin([], 3, 1)