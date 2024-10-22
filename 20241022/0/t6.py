

def f(x):
    pass

def run(gen):
    s = yield from gen
    print(f"/{s}/")

g = f("wecwe")
lst = run(g)
res = list(lst)
print(res)