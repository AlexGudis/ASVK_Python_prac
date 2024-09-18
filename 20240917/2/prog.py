summ = 0
x = int(input())
while x != 0 and x > 0:
    summ += x
    if summ > 21:
        print(summ)
        break
    x = int(input())
else:
    print(x)