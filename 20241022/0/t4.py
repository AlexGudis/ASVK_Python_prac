def pgen():
    print("Before")
    res = yield "Start"
    print(">")
    while res := ("yield" f"/{res}/"):
        print(">")
    yield "finish"
    print(">>")

g = pgen()
print(next(g))
for c in range(5, -1, -1):
    print(g.send(c))
