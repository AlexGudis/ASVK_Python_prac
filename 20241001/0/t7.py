def F(a, b):
    def fun(x):
        return a * x + b
    return fun
    
res = F(1,2)
print(res(3))