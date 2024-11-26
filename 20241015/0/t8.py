from math import *

s = input().split()
a, b = eval(input())
print(eval(s[0], None, {'x':a, "y":b}))
print(eval(s[0], None, {'x':b, "y":a}))