def travel(n):
    for _ in range(n):
        yield "по кочкам"
    return "и в яму"

def travelwrap(tr):
    yield (yield from tr)


w = travel(4)
wrap = travelwrap(w)
for el in wrap:
    print(el)
