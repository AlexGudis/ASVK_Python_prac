a = []

while str := input():
    a.append(list(eval(str)))
print(a)

if all(len(a[i]) == len(a) for i in range(len(a))):
    print('YES')
else:
    print("NO")

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        a[i][j], a[j][i] = a[j][i], a[i][j]

    

for i in range(len(a)):
    print(*a[i])