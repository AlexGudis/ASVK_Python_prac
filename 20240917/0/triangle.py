a,b,c = eval(input())
'''
if a > 0 and b > 0 and c > 0 and c < a + b and b < a + c and a < b + c:
    print("YES")
else:
    print("NO")
'''
print("YES" if a > 0 and b > 0 and c > 0 and c < a + b and b < a + c and a < b + c else "NO")