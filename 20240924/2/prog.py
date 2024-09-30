a = list(eval(input()))
for i in range(len(a)):
    a[i] = [int(a[i]) ** 2 % 100, int(a[i])]

swapped = True
while swapped:
    swapped = False
    for i in range(len(a) - 1):
        if a[i][0] > a[i+1][0]:
            a[i], a[i+1] = a[i+1], a[i]
            swapped = True

print([a[i][1] for i in range(len(a))])