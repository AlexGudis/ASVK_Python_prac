a = []
n = 1
check = True
while n:
    a.append(list(eval(input())))
    if check:
        n = len(a[0])
        check = False
    n -= 1

n = len(a[0])
b = []
while n:
    b.append(list(eval(input())))
    n -= 1

n = len(a[0])
ans = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        summ = 0
        for p in range(n):
            summ += a[i][p] * b[p][j]
        ans[i][j] = summ

for el in ans:
    print(*el, sep=',')
                