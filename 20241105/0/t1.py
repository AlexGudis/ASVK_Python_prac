class Rectangle:
    rectcnt = 0
    
    def __init__(self, x1, y1, x2, y2):
        self.__class__.rectcnt += 1
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        setattr(self, "rect_" + str(self.rectcnt), self.rectcnt)
        self.data = [(self.x1,self.y1),(self.x1,self.y2),(self.x2,self.y2),(self.x2, self.y1)]


    def get_sqr(self):
        return (abs(self.x2 - self.x1)) * (abs(self.y2 - self.y1))
        

    def __lt__(self, obj):
        return self.get_sqr() < obj.get_sqr()

    def __eq__(self, obj):
        return self.get_sqr() == obj.get_sqr()

    def __mul__(self, num):
        self.x1 *= num
        self.x2 *= num
        self.y1 *= num
        self.y2 *= num
        return self

    def __rmul__(self, num):
        self.__mul__(num)
        return self

    def __getitem__(self, ind):
        return self.data[ind]

    def __bool__(self):
        return self.get_sqr() != 0

    def __del__(self):
        self.__class__.rectcnt -= 1
        print('Объект удален. Число объектов = ', self.__class__.rectcnt)
        

    def __str__(self):
        return f'({self.x1}, {self.y1}),({self.x1}, {self.y2}),({self.x2}, {self.y2}),({self.x2}, {self.y1})'

def test():
    check = Rectangle(1,2,3,4)

if __name__ == '__main__':
    r = Rectangle(1,2,3,4)
    rr = Rectangle(5,6,7,100)
    #print(r.rectcnt)
    #print(getattr(r, "x1"))
    #print(dir(r))
    print(r < rr) # lt
    print(r == rr) # eq
    print(r * 2) # mul/rmul
    print(r[1]) # __getitem__
    # bool check
    if r:
        print('Not zero sqr')
    else:
        print('Zero sqr')
    test()

    
    



    
