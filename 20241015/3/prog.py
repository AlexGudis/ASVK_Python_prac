w = int(input())
words = dict()
maxx = 0
while s := input():
    s = list(s)
    for i in range(len(s)):
        if not s[i].isalpha():
            s[i] = ' '
    s = (''.join(s)).split()
    for el in s:
        if len(el.lower()) == w:
            words.setdefault(el.lower(), 0)
            words[el.lower()] += 1
            maxx = max(maxx, words[el.lower()])


words = dict(sorted(words.items()))
for k,v in words.items():
    if v == maxx:
        print(k, end=' ')
        
