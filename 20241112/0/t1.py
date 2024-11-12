class A:
    v = 1

class B(A):
    v = 2

b = B()
b.v = 3

print("Before = ", b.v)
del b.v
print("After del from obj = ", b.v)
del B.v
print("After del from class = ", B.v)