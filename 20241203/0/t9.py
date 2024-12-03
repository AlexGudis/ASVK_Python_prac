import inspect

class C:
    a: int
    def __init__(self, val):
        types = inspect.get_annotations(C)
        if not isinstance(val, types['a']):
            raise TypeError("Incorrect type")
        self.a = val


c = C(123)
print(c.a)
