from collections import Counter

magazine=        Counter(input().split())
small_text = Counter(input().split())

if len(small_text-magazine):
    print("NO")
else:
    print("YES")