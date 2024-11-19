from string import ascii_letters
import sys
import pympler
import pympler.asizeof


class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)



class Slotter:
    __slots__ = [el for el in ascii_letters]



t = Trad()
s = Slotter()

#print(dir(s))
print(f'sizeof t in sys = {sys.getsizeof(t)}')
print(f'sizeof s in sys = {sys.getsizeof(s)}')
print()
print(f'sizeof t in pympler = {pympler.asizeof.asizeof(t)}')
print(f'sizeof s in pympler = {pympler.asizeof.asizeof(s)}')