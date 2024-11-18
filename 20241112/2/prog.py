import math

class InvalidInput(Exception):
      pass


class BadTriangle(Exception):
     pass

def triangleSquare():
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(input())
    except Exception:
        raise InvalidInput
    
    check = [x1, y1, x2, y2, x3, y3]
    if not all( (isinstance(el, int) or isinstance(el, float)) for el in check ):
        raise BadTriangle
    
    a = math.sqrt( (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) )
    b = math.sqrt( (x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3) )
    c = math.sqrt( (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3) )

    p = (a + b + c) / 2

    s = math.sqrt( p * (p - a) * (p - b) * (p - c) )
    if not s:
        raise BadTriangle
    
    return s


while True:
    try:
        ans = triangleSquare()
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f'{ans:.2f}')
        break
