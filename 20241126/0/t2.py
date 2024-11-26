with open("data_ru", "rb") as f:
    s = f.read()
    ans = s[int(len(s) / 2):] + s[0:int(len(s) / 2)]

with open("data_ru", "wb") as f:
    print(ans)
    f.write(ans)