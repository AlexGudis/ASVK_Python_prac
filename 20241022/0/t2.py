def gen():
    summ = 0
    i = 1
    while True:
        summ += 1 / (i * i)
        yield summ
        i += 1

it = gen()
print(next(it))
print(next(it))
print(next(it))