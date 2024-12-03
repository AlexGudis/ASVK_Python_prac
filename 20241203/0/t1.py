'''class overtype(type):
    def __init__(self, Name, Parents, Dict):
        #print(f" Class definition: {Name}{Parents}: {Dict}")
        super().__init__(Name, Parents, Dict)

class C(metaclass=overtype):
    var = 100500
    def __init__(self, var=100500):
        self.var = var'''


C = type("C", (), {"__init__": lambda self, x=100500: setattr(self, "var", x)})

print(C.var)
c = C(123)
print(c.var)