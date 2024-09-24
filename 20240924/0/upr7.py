a,b = eval(input())
a = [i for i in range(a, b + 1) if i % 2 == 1 and '3' not in str(i)]
print(a)