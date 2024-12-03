class Doubeleton(type):
    _instance = []
    _i = -1
    def __call__(cls, *args, **kw):
        #print(f'Instance={cls._instance}')
        if len(cls._instance) < 2:
             cls._instance.append(super().__call__(*args, **kw))
        cls._i += 1
        return cls._instance[cls._i % 2]
    
class C(metaclass=Doubeleton): pass
print(*(C() for i in range(7)), sep="\n")