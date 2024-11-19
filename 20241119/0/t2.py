def isint(f):
    def newfun(*args):
        if not (all (isinstance(el, int) for el in args)):
            raise TypeError
        
        res = f(*args)
        return res
    return newfun


@isint
def fun(a,b):
    return a * 2 + b


print(fun(2,"cwcw"))