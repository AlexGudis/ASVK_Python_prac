def fill(a, b):
    ans = []
    for el in a:
        if el not in b:
            ans.append(el)
    return ans

def diff(a,b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    elif isinstance(a, list) and isinstance(b, list):
        return fill(a, b)
         
    elif isinstance(a, tuple) and isinstance(b, tuple):
        ans = fill(a,b)
        return tuple(ans)
    
a,b = eval(input())
print(diff(a,b))
