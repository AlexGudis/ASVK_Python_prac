class Vowel:
    __slots__ = ('a', 'e', 'i', 'o', 'u', 'y', '_answer')
    
    def __init__(self, **kwargs):
        for slot in self.__slots__:
            if slot != "_answer":
                setattr(self, slot, kwargs.get(slot, None))
        self._answer = 42

    @property
    def full(self):
        return all(object.__getattribute__(self, slot) is not None for slot in self.__slots__)

    @full.setter
    def full(self, value):
        raise AttributeError("ReadOnly!!!")

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        raise AttributeError("ReadOnly!!!")

    def __setattr__(self, key, value):
        if key not in self.__slots__:
            raise AttributeError(f"Cannot create '{key}', bc it isn't in __slots__")
        super().__setattr__(key, value)



    def __getattribute__(self, key):
        slots = object.__getattribute__(self, '__slots__')
        if key in slots and not key.startswith('_'):
            value = object.__getattribute__(self, key)
            if value is None:
                raise AttributeError(f"'{key}' slot is not set")
        return object.__getattribute__(self, key)



    def __str__(self):
        fields = {}
        for slot in self.__slots__:
            if slot[0] != '_':
                value = object.__getattribute__(self, slot)
                if value is not None:
                    fields[slot] = value
        result = ", ".join(f"{k}: {v}" for k, v in fields.items())
        return f"{result}"
    

import sys
exec(sys.stdin.read())