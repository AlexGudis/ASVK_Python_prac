class Sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError("Cannot have more than one parents")
        return super().__new__(metacls, name, parents, namespace)

class E(metaclass=Sole): pass
class C(metaclass=Sole): pass
class A(C, E): pass