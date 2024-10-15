s = input()
a, b = eval(input())
print(eval(s, None, {"x":a, "y":b}))
print(eval(s, None, {"x":b, "y":a}))