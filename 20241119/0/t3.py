def istype(typ):
    def decorator(fun):
        def newfun(*args):
            if all(isinstance(el, typ) for el in args):
                return [fun(*args)]
            return "NO."
        return newfun
    return decorator

@istype(int)
def simplefun(N):
    return N*2+1

print(simplefun("4"))