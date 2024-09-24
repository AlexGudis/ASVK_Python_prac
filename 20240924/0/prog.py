'''
l = list(range(5, 20))
print(l)
print(l[4])
print(l[4:6])
print(l[8:1:-2])
l[4:6] = range(20, 3, -3)
print(l)
'''

a = list(map(int, input().split()))
if 13 in a:
    print("YES")
else:
    print("NO")

print("YES" if 13 in a else "NO")
print(13 in eval(input()))