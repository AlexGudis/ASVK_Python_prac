def func(s="abcd abcd abcd"):
    s = s.split()
    d = {}
    for el in s:
        d.setdefault(el, 0)
        d[el] += 1
    return d