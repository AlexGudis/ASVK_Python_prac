class Counter:

    def __init__(self):
        self.c = 0
        

    def __get__(self, obj, cls):
        print(f"Get from {cls}:{repr(obj)}")
        return self.c

    def __set__(self, obj, val):
        print(f"Set in {repr(obj)} to {val}")
        self.c = val

class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        print("deleted")
        self.counter -= 1
        

c = C()
print(c.counter)

        
