# Сериализация
import pickle


class SerCls:
    def __init__(self, lst, dct, num, st):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st

    def __str__(self):
        return f'{self.lst} ||| {self.dct} ||| {self.num} ||| {self.st}'


class C:
    a = 1


ser = SerCls([1,2,3], {1:1, 2:2, 3:3}, 111, "wkcnwec")
print(ser)
data = pickle.dumps(ser,protocol=0)
del ser
serl = pickle.loads(data)
print(serl)
