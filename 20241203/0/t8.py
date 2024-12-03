import inspect


def fun(a: int, b: float=1.23) -> float:
    return a * b
print(fun.__annotations__)
print(inspect.get_annotations(fun))


class C:
    a: int = 100500
    b: float # аннотация есть, а поля нет)))

print(inspect.get_annotations(C))
#print(C.b)  