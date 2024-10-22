def walk_2d(x=0, y=0):
    while True:
        dx, dy= yield x, y
        x += dx
        y += dy

gen = walk_2d()
next(gen)
print(gen.send((0, 1)))
print(gen.send((-5, 12)))

