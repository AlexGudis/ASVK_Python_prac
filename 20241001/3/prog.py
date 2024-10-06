from math import *

def Calc(s,t,u):

    def s_fun(x):
        return eval(s)

    def t_fun(x):
        return eval(t)
    
    def fun(z):
        x = s_fun(z)
        y = t_fun(z)
        return eval(u)
    
    return fun

s = eval(input())
x = float(input())
F = Calc(s[0], s[1], s[2])
print(F(x))