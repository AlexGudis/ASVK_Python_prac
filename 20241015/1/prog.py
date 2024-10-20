s = input()
check = set()
for i in range(len(s) - 1):
    if s[i].isalpha() and s[i+1].isalpha():
        if (s[i].lower() + s[i+1].lower()) not in check:
            check.add((s[i].lower() + s[i+1].lower()))
print(len(check))
