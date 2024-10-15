s = input().split()
'''
d = {}
for el in s:
    d.setdefault(el)
for k, v in d.items():
    print(k, end=' ')
'''

print(*[k for k,v in {el:0 for el in s}.items()], end = ' ')