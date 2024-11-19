# не работает)

class Dumper:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, *args, **kwargs):
        '''
        print(args, kwargs, end=" → ")
        res = self.function(*args, **kwargs)
        print(res)
        return res
        '''
        def decorator(fun):
            if not all(isinstance(el, self.typ) for el in args):
                raise TypeError
            return fun(*args, **kwargs)
        return decorator
    

@Dumper(int)
def add(x, y, z):
    return x + y + z

print(add(3,4,5))