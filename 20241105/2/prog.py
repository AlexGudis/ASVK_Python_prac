import math


class Triangle:

    def get_side(self, x1, x2, y1, y2):
        return math.sqrt((x2- x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    def __init__(self, t1, t2, t3):
        self.x1, self.y1 = t1
        self.x2, self.y2 = t2
        self.x3, self.y3 = t3
        self.p1 = t1
        self.p2 = t2
        self.p3 = t3
        self.a = self.get_side(self.x1, self.x2, self.y1, self.y2)
        self.b = self.get_side(self.x1, self.x3, self.y1, self.y3)
        self.c = self.get_side(self.x2, self.x3, self.y2, self.y3)

    def check_tr(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a
    
    def __abs__(self):
        if not self.check_tr():
            return 0
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def __bool__(self):
        return bool(abs(self))
    
    def __lt__(self, obj):
        return abs(self) < abs(obj)

    def point_in(self, point):
        check1 = (self.x1 - point[0]) * (self.y2 - point[1]) - (self.x2 - point[0]) * (self.y1 - point[1])
        check2 = (self.x2 - point[0]) * (self.y3 - point[1]) - (self.x3 - point[0]) * (self.y2 - point[1])
        check3 = (self.x3 - point[0]) * (self.y1 - point[1]) - (self.x1 - point[0]) * (self.y3 - point[1])
        
        sign = lambda x: math.copysign(1, x) # two will work
        if sign(check1) == sign(check2) == sign(check3):
            return True # point in treangle
        return False
    
    def __contains__(self, item):
        if self is item:
            return True

        if not abs(item):
            return True

        if all(self.point_in(p) for p in (item.p1, item.p2, item.p3)): 
            return True

        return False

        
        

    def __and__(self, other):
        if not abs(self) or not abs(other):
            return False 

        for el in (self.p1, self.p2, self.p3):
            if other.point_in(el):
                return True

        for el in (other.p1, other.p2, other.p3):
            if self.point_in(el):
                return True
        
        return False
        

    
'''
r = Triangle((4, 2), (1, 3), (2, 4))
s = Triangle((1, 1), (3, 1), (2, 2))
t = Triangle((0, 0), (2, 3), (4, 0))
o = Triangle((1, 1), (2, 2), (3, 3))

print(*(f"{n}({bool(x)}):{round(abs(x), 3)}" for n, x in zip("rsto", (r, s, t, o))))
print(f"{s < t=}, {o < t=}, {r < t=}, {r < s=}")
print(f"{s in t=}, {o in t=}, {r in t=}")
print(f"{r & t=}, {t & r=}, {s & r=}, {o & t=}")
'''


import sys
exec(sys.stdin.read())