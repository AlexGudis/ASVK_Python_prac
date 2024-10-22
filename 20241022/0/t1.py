def gen(x):
    yield x
    yield x + 1
    yield "DONE"

e = gen(2)
print(next(e))
for i in e:
    print(i)
print(next(e))