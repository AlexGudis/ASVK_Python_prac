class Omnibus:
    info = {}

    def __init__(self):
        super().__setattr__("info_loc", set()) # install local pool of attrs to obj

    def __getattr__(self, name):
        if name[0] != '_' and name in self.__class__.info:
            return self.__class__.info[name]
    

    def __setattr__(self, name, value):
        if name[0] != '_':
            self.__class__.info.setdefault(name, 0)
            self.__class__.info[name] += 1 
            self.info_loc.add(name)
 

    def __delattr__(self, name):
        if name[0] != '_' and name in self.info_loc:
            self.info_loc.remove(name)
            if name in self.__class__.info:
                self.__class__.info[name] -= 1 
                if self.__class__.info[name] <= 0:
                    self.__class__.info.pop(name) 

import sys
exec(sys.stdin.read())