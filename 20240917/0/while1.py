cnt, i = 0, 1
x = int(input())
while x != 0:
    if x == i:
        cnt += 1
    x = int(input())
    i += 1
print(cnt)