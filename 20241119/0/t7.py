class C:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        """I'm the 'x' property."""
        if self._age == 42:
            print("secret value!")
            return -1
        return self._age

    @age.setter
    def age(self, value):
        print(f"Setter with value {value}")
        if value <= 128:
            self._age = value
        else:
            print("Too old!")
            raise ValueError

    @age.deleter
    def age(self):
        del self.age


c = C()
c.age = 12
c.age = 129
print(c.age)