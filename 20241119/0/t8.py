class Slo:
    __slots__ = "a", "b", "c"
    readonly = 100500

    def __init__(self, x, y, z):
        self.a, self.b, self.c = x, y, z