class Num:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, 0)

    def __set__(self, instance, value):
        if hasattr(value, "real"):
            setattr(instance, self.private_name, value)
        elif hasattr(value, "__len__"):
            setattr(instance, self.private_name, len(value))


import sys
exec(sys.stdin.read())