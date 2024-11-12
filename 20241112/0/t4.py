C = type("C", (), {"a":100500, "fun": lambda self: self.a, "__init__": lambda self, val: setattr(self, "a", val)})
print(C(123).a)
print(C.a)